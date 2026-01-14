from django.db import models
from accounts.models.trainer import Trainer
from branches.models.branch import Branch

class WorkOutPlan(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    created_by = models.ForeignKey(Trainer, on_delete=models.CASCADE, null = True,blank = True, related_name = "workout_plans")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
                                      