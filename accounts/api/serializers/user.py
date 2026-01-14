from rest_framework import serializers
from accounts.models.custome_user import User

class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[('admin', 'Admin'),('manager', 'Manager'), ('member', 'Member'), ('trainer', 'Trainer')], required=True)

    class Meta:
        model = User
        fields = ("email", "password", "is_active", "is_staff", "is_verified", "role")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user