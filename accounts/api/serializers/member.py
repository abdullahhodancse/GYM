from rest_framework import serializers
from accounts.models.member import Member

class MemberSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    

    class Meta:
        model = Member
        fields = ["id", "user_id", "branch", "phone_number", "address", "created_at"]

        read_only_fields = ["id", "created_at"]