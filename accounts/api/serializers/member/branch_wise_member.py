from rest_framework import serializers
from accounts.models.member import Member

class BranchWiseMemberListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    role = serializers.CharField(source="user.role", read_only=True)
    branch_name = serializers.CharField(source="branch.name", read_only=True)

    class Meta:
        model = Member
        fields = ["id", "email", "role", "branch_name"]