# accounts/api/view/trainer_list.py
from rest_framework import generics
from accounts.models.trainer import Trainer
from accounts.api.serializers.trainer.trainer_list import TrainerListSerializer
from admin_permission import IsAdmin 

class TrainerListView(generics.ListAPIView):
    serializer_class = TrainerListSerializer
    queryset = Trainer.objects.select_related("branch", "user")
    permission_classes = [IsAdmin]



    def get_queryset(self):
        return Trainer.objects.filter(
            user__role="trainer"
        ).select_related("branch", "user")
