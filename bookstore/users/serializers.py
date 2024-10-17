from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from users.services.token_services import TokenService

from mainapp.models import CustomUser

from .user_services import UserServices


class UserSignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    user_type = serializers.CharField()

    def create(self, validated_data):
        email = validated_data.get("email")
        username = validated_data.get("username")
        password = validated_data.get("password")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        user_type = validated_data.get("user_type")

        user = UserServices.create_user(
            self=self,
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
        )

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "first_name", "last_name"]
