 # workouts/api/serializers/member_assigned_workout.py

from rest_framework import serializers
from workouts.models.memberworkOut import MemberWorkOut
from workouts.api.serializer.work_out__task import WorkoutTaskCreateSerializer


class MemberAssignedWorkoutListSerializer(serializers.ModelSerializer):
    plan_title = serializers.CharField(
        source="workoutplan.title",
        read_only=True
    )
    plan_description = serializers.CharField(
        source="workoutplan.description",
        read_only=True
    )
    tasks =WorkoutTaskCreateSerializer(
        source="workoutplan.workout_tasks",
        many=True,
        read_only=True
    )

    class Meta:
        model = MemberWorkOut
        fields = [
            "id",
            "plan_title",
            "plan_description",
            "status",
            "due_date",
            "tasks",
        ]
