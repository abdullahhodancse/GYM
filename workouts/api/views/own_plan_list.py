# workouts/api/views/member_assigned_workout.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from workouts.models.memberworkOut import MemberWorkOut
from workouts.api.serializer.own_plan_list import MemberAssignedWorkoutListSerializer
from permissions.member_permission import IsMember
from pagination import Pagination
   



class MemberAssignedWorkoutListView(generics.ListAPIView):
    serializer_class = MemberAssignedWorkoutListSerializer
    permission_classes = [IsMember]
    pagination_class = Pagination

    def get_queryset(self):
        return (
            MemberWorkOut.objects
            .filter(member=self.request.user.member)
            .select_related("workoutplan")
            .prefetch_related("workoutplan__workout_tasks")
        )
