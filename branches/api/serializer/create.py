from rest_framework import serializers
from branches.models.branch import Branch


class BranchSerializer(serializers.ModelSerializer):

    manager = serializers.CharField(source="manager.user.email", allow_null=True)  # manager er email ta dekhanor jjonno.
    class Meta:
        model = Branch
        fields = ["id", "name", "address","phone_number","manager", "created_at"]
        read_only_fields = ["id", "created_at"]