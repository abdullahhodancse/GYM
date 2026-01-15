# workouts/api/serializer/plan_assign_to_member.py

from rest_framework import serializers
from workouts.models.memberworkOut import MemberWorkOut
from workouts.models.workOut_plan import WorkOutPlan
from accounts.models.member import Member


class MemberWorkoutAssignSerializer(serializers.ModelSerializer):
    workout_plan_id = serializers.IntegerField(write_only=True)
    member_id = serializers.IntegerField(write_only=True)
    due_date = serializers.DateField()

    class Meta:
        model = MemberWorkOut
        fields = ["workout_plan_id", "member_id", "due_date"]

    def validate(self, data):
        request = self.context["request"]
        trainer = request.user.trainer

        workout_plan = WorkOutPlan.objects.get(id=data["workout_plan_id"])
        member = Member.objects.get(id=data["member_id"])

        if workout_plan.created_by_id != trainer.id:
            raise serializers.ValidationError(
                "You can assign only your own workout plan"
            )

        if member.branch_id != trainer.branch_id:
            raise serializers.ValidationError(
                "You can assign only members from your branch"
            )

        data["workoutplan"] = workout_plan
        data["member"] = member
        return data

    def create(self, validated_data):
        validated_data.pop("workout_plan_id")
        validated_data.pop("member_id")
        return MemberWorkOut.objects.create(**validated_data)
