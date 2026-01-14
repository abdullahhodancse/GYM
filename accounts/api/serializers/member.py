from rest_framework import serializers
from accounts.models.member import Member

class MemberSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Member
        fields = ["id", "branch", "phone_number", "address", "created_at"]

        read_only_fields = ["id", "created_at"]