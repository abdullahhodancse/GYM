

from rest_framework import generics
from workouts.models.workOut_plan import WorkOutPlan
from workouts.api.serializer.work_out_plan_show import (WorkOutPlanWithTaskSerializer)
from manager_permission import IsManager
from adminOrManager_permission import IsAdminOrManager


class WorkoutPlanListView(generics.ListAPIView):
    serializer_class = WorkOutPlanWithTaskSerializer
    permission_classes = [IsAdminOrManager]
    

    def get_queryset(self):
        return (
            WorkOutPlan.objects
            .select_related("created_by", "branch")
            .prefetch_related("workout_tasks")
        )
