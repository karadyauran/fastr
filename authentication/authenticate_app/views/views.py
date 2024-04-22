import requests
from django.core.cache import cache
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.authtoken.models import Token

from authentication.authenticate_app.management.commands.send_kafka_messages import Command
from authentication.authenticate_app.models.auth_user import UserAuth
from authentication.authenticate_app.serializers.serializer import UserAuthSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup(request):
    """ Sign up for new user. """
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.create(request.data)
        token, created = Token.objects.get_or_create(user=user)
        cache.set(f'token_{user.id}', token, timeout=3600 * 4)

        url = 'http://cart:8003/api/v1/cart/create_cart'
        data = {'token': token.key}
        requests.post(url, data=data)

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

    token_key = cache.get(f'token_{auth_user.id}')
    if not token_key:
        token, created = Token.objects.get_or_create(user=auth_user)
        token_key = token.key
        cache.set(f'token_{auth_user.id}', token_key, timeout=3600*4)

    kafka_data = {
        'email': auth_user.email,
        'first_name': auth_user.first_name,
    }

    cmd = Command()
    cmd.kafka_producer('localhost:9092', 'auth-topic', data=kafka_data)

    return Response({"token": str(token_key), "user": UserAuthSerializer(auth_user).data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def logout(request):
    """ Log out user from session """
    try:
        request.user.is_active = False
        request.user.save()

        cache.delete(f'token_{request.user.id}')

        request.user.auth_token.delete()

        return Response({'detail': f'Successfully logged out for {request.user.email}.'}, status=status.HTTP_200_OK)
    except (AttributeError, Token.DoesNotExist):
        return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
