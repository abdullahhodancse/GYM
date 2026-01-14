from rest_framework import serializers
from branches.models.branch import Branch

class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ["id", "name", "address","phone_number", "created_at"]
        read_only_fields = ["id", "created_at"]
