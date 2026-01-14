# accounts/api/serializers/trainer/list.py
from rest_framework import serializers
from accounts.models.trainer import Trainer

class TrainerListSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source="branch.name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    role = serializers.CharField(source="user.role", read_only=True)

    class Meta:
        model = Trainer
        fields = [
            "id",
            "email",
            "role",
            "branch_name",
        ]
