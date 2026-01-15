# workouts/api/views/trainer_workout_plan.py
from rest_framework.generics import CreateAPIView
from workouts.api.serializer.work_out_plan import  WorkOutPlanSerializer
from permissions.trainer_permission import IsTrainer

class TrainerWorkoutPlanCreateView(CreateAPIView):
    serializer_class = WorkOutPlanSerializer
    permission_classes = [IsTrainer]
