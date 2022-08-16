from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.settings import APISettings
from rest_framework_jwt.settings import api_settings


from .models import User
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER

JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


User = get_user_model()

class UserCreateSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields='__all__'
        
    # email = serializers.EmailField(required=True)
    # username = serializers.CharField(required=True)
    # password = serializers.CharField(required=True)

    def create(self, validated_data):
        # user = User.objects.create(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        # )
        # user.set_password(validated_data['password'])

        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User(
            email=email
        )
        user.set_password(password)

        user.save()
        return user
    
""" class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        } """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'