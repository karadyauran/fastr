from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers import UserSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# GET requests
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_address(request):
    user = get_object_or_404(User, id=request.user.id)
    return Response({'address': request.user.address}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_location(request):
    user = get_object_or_404(User, id=request.user.id)
    return Response({'address': request.user.location}, status=status.HTTP_200_OK)


# Delete user

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def delete_user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    user.delete()
    return Response({'detail': f'Successfully deleted profile for {request.user.email}.'}, status=status.HTTP_200_OK)


# PATCH requests

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def change_user_profile_image(request):
    user = get_object_or_404(User, id=request.user.id)
    user.image = request.query_params.get('image')
    user.save()
    return Response({'detail': f'Successfully changed image for {request.user.email}.'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def change_user_profile_location(request):
    user = get_object_or_404(User, id=request.user.id)
    user.location = request.query_params.get('location')
    user.save()
    return Response({'detail': f'Successfully changed location for {request.user.email}.'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def change_user_profile_email(request):
    user = get_object_or_404(User, id=request.user.id)

    if not User.objects.filter(email=request.user.email).exists():
        user.email = request.query_params.get('email')
        user.save()
        return Response({'detail': f'Successfully changed email for {request.user.email}.'},
                        status=status.HTTP_200_OK)
    return Response({'detail': f'Email is already exists'}, status=status.HTTP_400_BAD_REQUEST)
