from rest_framework import serializers
from authentication.authenticate_app.models.auth_user import UserAuth


class UserAuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta(object):
        model = UserAuth
        fields = '__all__'

    def create(self, validated_data):
        user = UserAuth.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        if 'location' in validated_data:
            user.set_location(validated_data['location'])

        user.set_password(validated_data['password'])
        user.save()

        return user
