from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.authtoken.models import Token

from authentication.authenticate_app.management.commands.send_kafka_messages import Command
from authentication.authenticate_app.models.auth_user import UserAuth
from authentication.authenticate_app.serializers.cart_serializer import CartSerializer
from authentication.authenticate_app.serializers.serializer import UserAuthSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from settings.base_settings import KAFKA_BOOTSTRAP_SERVERS


def get_user_id(request=None, token=None):
    """ Extract user ID from request token """
    if not token:
        token_key = request.headers.get('Authorization').split()[1]
        token = get_object_or_404(Token, key=token_key)
    return token.user.id


def create_cart(token):
    user_id = get_user_id(token=token)
    serializer = CartSerializer(data={
        'user': user_id,
    })

    if serializer.is_valid():
        serializer.save()


@api_view(['POST'])
def signup(request):
    """ Sign up for new user. """
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.create(request.data)
        token, created = Token.objects.get_or_create(user=user)
        create_cart(token)

        serialized_user = UserAuthSerializer(user).data

        return Response({"token": token.key, "user": serialized_user}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """ Login for new user. """
    auth_user = get_object_or_404(UserAuth, username=request.data['username'])
    if not auth_user.check_password(request.data['password']):
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

    auth_user.is_active = True
    auth_user.last_login = timezone.now()
    auth_user.save()

    token, created = Token.objects.get_or_create(user=auth_user)
    serialized_user = UserAuthSerializer(auth_user).data

    # cmd = Command()
    # cmd.kafka_producer(KAFKA_BOOTSTRAP_SERVERS, 'auth-topic', data={
    #     'email': auth_user.email,
    #     'first_name': auth_user.first_name,
    # })

    return Response({"token": token.key, "user": serialized_user}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def logout(request):
    """ Log out user from session """
    try:
        request.user.is_active = False
        request.user.save()

        request.user.auth_token.delete()

        return Response({'detail': f'Successfully logged out for {request.user.email}.'}, status=status.HTTP_200_OK)
    except (AttributeError, Token.DoesNotExist):
        return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
