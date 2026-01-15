from rest_framework import generics
from workouts.models.memberworkOut import MemberWorkOut
from workouts.api.serializer.status_update_by_trainer import MemberWorkoutStatusUpdateSerializer
from trainer_permission import IsTrainer


class MemberWorkoutStatusUpdateView(generics.UpdateAPIView):
    serializer_class = MemberWorkoutStatusUpdateSerializer
    permission_classes = [IsTrainer]
    http_method_names = ["patch"]

    def get_queryset(self):
        trainer = self.request.user.trainer
        return MemberWorkOut.objects.filter(
            workoutplan__created_by=trainer,
            workoutplan__branch=trainer.branch
        )
