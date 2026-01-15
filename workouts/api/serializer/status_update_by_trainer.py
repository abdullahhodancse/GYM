from rest_framework import serializers
from workouts.models.memberworkOut import MemberWorkOut


class MemberWorkoutStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberWorkOut
        fields = ["status"]