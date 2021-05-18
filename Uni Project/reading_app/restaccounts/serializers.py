from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    EmailField,
)

from restaccounts.models import DriverUser

class RegisterSerializer(ModelSerializer):
    email = EmailField(label='Email address')
    class Meta:
        model = DriverUser
        fields = [
            'id',
            'username',
            'email',
            'user_type',
            'password',
        ]
    extra_kwargs = {
        "password": {"write_only":True},
        "id": {"read-only":True}
    }

    def validate(self, data):
        return data

    def validate_email(self, value):
        email = value
        user_qs = DriverUser.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Email already registered")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user_type = validated_data['user_type']
        user_obj = DriverUser(
            username = username,
            email = email,
            user_type = user_type,
        )

        user_obj.set_password(password)
        user_obj.save()
        return user_obj