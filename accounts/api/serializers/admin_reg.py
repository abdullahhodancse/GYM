from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    secret_key = serializers.CharField(write_only=True)

    def validate_secret_key(self, value):
        if value != settings.ADMIN_REG_SECRET:
            raise serializers.ValidationError("Invalid admin secret key")
        return value

    def create(self, validated_data):
        validated_data.pop("secret_key")

        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            role="admin",
            is_staff=True,
            is_superuser=True
        )
        return user
