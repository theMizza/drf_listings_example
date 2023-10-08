from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Accounts

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create User and Accounts models objects method"""
        print(validated_data)
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        user.username = validated_data.pop('email', None)
        if password is not None:
            user.set_password(password)
        user.save()
        Accounts.objects.create(user=user)
        return user
