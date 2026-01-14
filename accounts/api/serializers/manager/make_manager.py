# accounts/api/serializers/manager.py
from rest_framework import serializers
from accounts.models.custome_user import User
from accounts.models.manager import Manager
from branches.models.branch import Branch


class MemberToManagerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    branch_id = serializers.IntegerField()

    def validate(self, data):
        # user check
        try:
            user = User.objects.get(id=data["user_id"])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if user.role != "member":
            raise serializers.ValidationError("Only member can be promoted to manager")

        # branch check
        try:
            branch = Branch.objects.get(id=data["branch_id"])
        except Branch.DoesNotExist:
            raise serializers.ValidationError("Branch not found")

        # branch already has manager?
        if Manager.objects.filter(branch=branch).exists():
            raise serializers.ValidationError("This branch already has a manager")

        return data

    def create(self, validated_data):
        user = User.objects.get(id=validated_data["user_id"])
        branch = Branch.objects.get(id=validated_data["branch_id"])

        # role update
        user.role = "manager"
        user.save()

        # manager create
        manager = Manager.objects.create(
            user=user,
            branch=branch
        )
        return manager
    
    def to_representation(self, instance):
        return {
            "manager_name":  instance.user.email,
            "branch_name": instance.branch.name
        }
