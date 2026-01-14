from rest_framework import serializers
from workouts.models.workOut_plan import WorkOutPlan
from workouts.api.serializer.work_out__task import WorkoutTaskCreateSerializer


class WorkOutPlanWithTaskSerializer(serializers.ModelSerializer):
    tasks = WorkoutTaskCreateSerializer(
        source="workout_tasks", many=True, read_only=True
    )

    class Meta:
        model = WorkOutPlan
        fields = ["id", "title", "description", "tasks"]