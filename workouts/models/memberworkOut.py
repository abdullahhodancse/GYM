from django.db import models
from accounts.models.member import Member
from workouts.models.workOut_plan import WorkOutPlan


class MemberWorkOut(models.Model):

    STATUS_CHOICES  = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        
    ]

    workoutplan = models.ForeignKey(WorkOutPlan,on_delete=models.CASCADE,null = True,blank = True, related_name = "member_workouts")
    member = models.ForeignKey(Member,on_delete=models.CASCADE,null = True,blank = True, related_name = "member")
    status = models.CharField(max_length = 20,choices = STATUS_CHOICES,default="pending")

    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("workoutplan", "member")  # ensure that a member can not added for same workout plan

    def __str__(self):
        return f"{self.member.user.email} - {self.workoutplan.title}"

                                    