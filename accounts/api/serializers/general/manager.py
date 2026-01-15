from rest_framework import serializers
from accounts.models.manager import Manager

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ["id", "branch", "phone_number", "address", "created_at"]
        read_only_fields = ["id", "created_at"]  #unchangeable
