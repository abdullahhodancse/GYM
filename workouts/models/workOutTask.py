from django.db import models
from workouts.models.workOut_plan import WorkOutPlan


class WorkOutTask(models.Model):
    workplan = models.ForeignKey(WorkOutPlan,on_delete = models.CASCADE,null = True, blank = True, related_name = "workout_tasks")
    name = models.CharField(max_length = 100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.workplan.title})"




