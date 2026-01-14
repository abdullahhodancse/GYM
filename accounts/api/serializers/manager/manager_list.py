from rest_framework import serializers
from accounts.models.manager import Manager

class ManagerListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    role = serializers.CharField(source="user.role")
    branch_name = serializers.CharField(source="branch.name",allow_null=True)

    class Meta:
        model = Manager
        fields = [
            "id",
            "email",
            "role",
            "branch_name",
        ]


        
