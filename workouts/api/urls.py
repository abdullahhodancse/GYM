from workouts.api.views.work_out_plan import TrainerWorkoutPlanCreateView
from workouts.api.views.workout_task import WorkoutTaskCreateView
from workouts.api.views.work_out_plan_show import WorkoutPlanListView
from workouts.api.views.plan_aasing_to_member import AssignMemberToWorkoutPlanView
from workouts.api.views.own_plan_list import MemberAssignedWorkoutListView
from workouts.api.views.status_update_by_trainer import MemberWorkoutStatusUpdateView

from django.urls import path

urlpatterns = [
    path("trainer/workout_plan/create/", TrainerWorkoutPlanCreateView.as_view(),name = "trainer_workout_plan_create"),
    path("trainer/workout_task/create/", WorkoutTaskCreateView.as_view(),name = "trainer_workout_task_create"),
    path("workout-plans/list/", WorkoutPlanListView.as_view(), name="workout-plan-list"),
    path("assign_plan_member/",AssignMemberToWorkoutPlanView.as_view(),name = "assign_task_member"),
    path("own_plan_list/",MemberAssignedWorkoutListView.as_view(),name ="own_list"),
    path("own_status_update/<int:pk>/", MemberWorkoutStatusUpdateView.as_view(),name="own_status_update")
]


