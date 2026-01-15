# workouts/api/views/member_workout_assign.py

from rest_framework import generics
from workouts.models.memberworkOut import MemberWorkOut
from workouts.api.serializer.plan_assaing_to_member import  MemberWorkoutAssignSerializer
from permissions.trainer_permission import IsTrainer


class AssignMemberToWorkoutPlanView(generics.CreateAPIView):
    queryset =MemberWorkOut.objects.all()
    serializer_class = MemberWorkoutAssignSerializer
    permission_classes = [ IsTrainer]

    def get_serializer_context(self):
        return {"request": self.request}
