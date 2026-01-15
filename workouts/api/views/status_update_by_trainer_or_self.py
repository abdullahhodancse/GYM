from rest_framework import generics
from workouts.models.memberworkOut import MemberWorkOut
from workouts.api.serializer.status_update_by_trainer_or_self import MemberWorkoutStatusUpdateSerializer
from permissions.memberOrTrainer import IsMemberOrTrainer


class MemberWorkoutStatusUpdateView(generics.UpdateAPIView):
    serializer_class = MemberWorkoutStatusUpdateSerializer
    permission_classes = [IsMemberOrTrainer]
    http_method_names = ["patch"]

    def get_queryset(self):
        user = self.request.user

        # member can chnage own status
        if hasattr(user, "member"):
            return MemberWorkOut.objects.filter(
                member=user.member
            )

        # trainer can change the status which is his own made and his won branche
        if hasattr(user, "trainer"):
            trainer = user.trainer
            return MemberWorkOut.objects.filter(
                workoutplan__created_by=trainer,
                workoutplan__branch=trainer.branch
            )

        return MemberWorkOut.objects.none()
