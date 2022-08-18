from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data): # 회원가입
        login_id = validated_data.get('login_id')
        password = validated_data.get('password')
        email = validated_data.get('email')
        
        user = User(
            login_id=login_id,
            email = email,
        )
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
