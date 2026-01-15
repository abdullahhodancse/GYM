
from  permissions.trainer_permission import IsTrainer
from workouts.models.workOutTask import WorkOutTask
from workouts.api.serializer.work_out__task import WorkoutTaskCreateSerializer

from rest_framework import generics



class WorkoutTaskCreateView(generics.CreateAPIView):
    queryset = WorkOutTask.objects.all()
    serializer_class = WorkoutTaskCreateSerializer
    permission_classes = [IsTrainer]


     # provite extra data 
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context