from rest_framework import serializers
from .models import ProfileUser
from auth_app.serializers import UserSerializer


class ProfileUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    img = serializers.CharField()

    class Meta:
        model = ProfileUser
        fields = ['user', 'img']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = representation.pop('user')
        for key, value in user_representation.items():
            representation[key] = value
        return representation

