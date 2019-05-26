from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Profile
from django.contrib.auth.models import User


class RegisterUserSerialzier(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=100, write_only=True)
    email = serializers.CharField(max_length=100,write_only=True)
    serial = serializers.CharField(max_length=10, write_only=True)
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100, write_only=True)
    userRole = serializers.CharField(max_length=1, default='S', write_only=True)

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).exists() or \
           User.objects.filter(email=validated_data['email']).exists() or \
           Profile.objects.filter(serial=validated_data['serial']).exists():
            raise ValidationError({"message": "Duplicate"})

        new_user = User.objects.create(username=validated_data['username'],
                                       email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'])
        new_user.set_password(validated_data['password'])
        print(validated_data)
        new_profile = Profile.objects.create(
            user=new_user,
            userRole=validated_data['userRole'],
            serial=validated_data['serial'],
        )

        if (validated_data['userRole'] == Profile.Student):
            new_profile.verified = True
            new_profile.save()

        return {
            'username' : new_user.username,
        }
