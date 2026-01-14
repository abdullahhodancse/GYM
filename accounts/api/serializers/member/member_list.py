# accounts/api/serializers/member/assign_branch.py
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from accounts.models.member import Member
from django.contrib.auth import get_user_model

User = get_user_model()

class AssignMemberToBranchSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        request = self.context["request"]

        # ensure manager
        if not hasattr(request.user, "manager"):
            raise ValidationError("Only manager can assign member to branch")

        # find user by email
        try:
            user = User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise ValidationError({
                "email": "User with this email does not exist"
            })

        # find member profile
        try:
            member = Member.objects.get(user=user)
        except Member.DoesNotExist:
            raise ValidationError({
                "email": "This user is not a member"
            })

        attrs["member"] = member
        attrs["branch"] = request.user.manager.branch
        return attrs

    def save(self, **kwargs):
        member = self.validated_data["member"]
        branch = self.validated_data["branch"]

        member.branch = branch
        member.save()
        return member
