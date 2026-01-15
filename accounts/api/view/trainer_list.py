# accounts/api/view/trainer_list.py
from rest_framework import generics
from accounts.models.trainer import Trainer
from accounts.api.serializers.trainer.trainer_list import TrainerListSerializer
from permissions.admin_permission import IsAdmin 
from pagination import Pagination

class TrainerListView(generics.ListAPIView):
    serializer_class = TrainerListSerializer
    queryset = Trainer.objects.select_related("branch", "user")
    permission_classes = [IsAdmin]
    pagination_class = Pagination



    def get_queryset(self):
        return Trainer.objects.filter(
            user__role="trainer"
        ).select_related("branch", "user")
