# accounts/api/serializers/promote_trainer.py
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from accounts.models.member import Member
from accounts.models.trainer import Trainer

class MakeTrainerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def validate(self, attrs):
        request = self.context["request"]

        # ensure manager
        if not hasattr(request.user, "manager"):
            raise ValidationError("Only manager can promote member to trainer")

        manager = request.user.manager
        branch = manager.branch

        # member exists
        try:
            member = Member.objects.get(user_id=attrs["user_id"])
        except Member.DoesNotExist:
            raise ValidationError("Member not found")

        # already trainer check
        if Trainer.objects.filter(user=member.user).exists():
            raise ValidationError("Member is already a trainer")

        # max 3 trainer in manager branch
        if Trainer.objects.filter(branch=branch).count() >= 3:
            raise ValidationError("Maximum 3 trainers allowed in a branch")

        attrs["member"] = member
        attrs["branch"] = branch
        return attrs

    def create(self, validated_data):
        member = validated_data["member"]
        branch = validated_data["branch"]
        user = member.user

        # update user role
        user.role = "trainer"
        user.save()

        # create trainer in MANAGER branch
        trainer = Trainer.objects.create(
            user=user,
            branch=branch
        )
        return trainer
    

    # manger onno manager k trainer hisebe promote korte parbe na
