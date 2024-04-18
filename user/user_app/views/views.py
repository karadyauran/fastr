from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.authenticate_app.models.auth_user import UserAuth
from authentication.authenticate_app.serializers.serializer import UserAuthSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cart.cart_app.models.cart_model import Cart


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_profile(request):
    """ Get user profile """
    user = get_object_or_404(UserAuth, id=request.user.id)
    serializer = UserAuthSerializer(instance=user)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def delete_user_profile(request):
    """ Delete user profile """
    user = get_object_or_404(UserAuth, id=request.user.id)
    cart = Cart.objects.filter(user=user).first()
    cart.delete()
    user.delete()
    return Response({'detail': f'Successfully deleted profile for {request.user.email}.'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def change_user_profile_image(request):
    """ Change user profile image """
    user = get_object_or_404(UserAuth, id=request.user.id)
    user.profile_photo = request.query_params.get('image')
    user.save()
    return Response({'detail': f'Successfully changed image for {request.user.email}.'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def change_user_profile_location(request):
    """ Change user profile location """
    user = get_object_or_404(UserAuth, id=request.user.id)
    user.location = request.query_params.get('location')
    user.save()
    return Response({'detail': f'Successfully changed location for {request.user.email}.'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def change_user_profile_email(request):
    """ Change user profile email """
    user = get_object_or_404(UserAuth, id=request.user.id)

    if not UserAuth.objects.filter(email=request.query_params.get('email')).exists():
        user.email = request.query_params.get('email')
        user.save()
        return Response({'detail': f'Successfully changed email for {request.user.email}.'},
                        status=status.HTTP_200_OK)
    return Response({'detail': f'Email is already exists'}, status=status.HTTP_400_BAD_REQUEST)
