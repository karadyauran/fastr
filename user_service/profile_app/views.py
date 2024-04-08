from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import ProfileUser
from .serializers import ProfileUserSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models.signals import post_save
from django.dispatch import receiver


# Receivers
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profileuser.save()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_profile(request):
    user = get_object_or_404(ProfileUser, id=request.user.id)
    serializer = ProfileUserSerializer(instance=user)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def delete_user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    user.delete()
    return Response({'detail': f'Successfully deleted profile for {request.user.email}.'}, status=status.HTTP_200_OK)
