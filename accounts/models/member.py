from django.db import models
from accounts.models.custome_user import User
from branches.models.branch import Branch
from django.utils import timezone

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL,null = True,blank = True)  #one branch many members
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user.email
