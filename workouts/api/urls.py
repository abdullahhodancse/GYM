from workouts.api.views.work_out_plan import TrainerWorkoutPlanCreateView
from django.urls import path

urlpatterns = [
    path("trainer/workout_plan/create/", TrainerWorkoutPlanCreateView.as_view(),name = "trainer_workout_plan_create"),
]


