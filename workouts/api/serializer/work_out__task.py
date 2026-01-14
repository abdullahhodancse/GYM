# workouts/api/serializers/workout_task.py

from rest_framework import serializers
from workouts.models.workOutTask import WorkOutTask
from workouts.models.workOut_plan import WorkOutPlan


class WorkoutTaskCreateSerializer(serializers.ModelSerializer):
    plan_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WorkOutTask
        fields = ["plan_id", "name", "sets", "reps"]

    def validate(self, data):
        trainer = self.context["request"].user.trainer
        plan = WorkOutPlan.objects.get(id=data["plan_id"])

    
        if plan.created_by_id != trainer.id:
            raise serializers.ValidationError(
                "You can add task only to your own workout plan"
            )

        data["workplan"] = plan
        return data

    def create(self, validated_data):
        validated_data.pop("plan_id")
        return WorkOutTask.objects.create(**validated_data)
