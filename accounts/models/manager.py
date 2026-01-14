from django.db import models
from django.utils import timezone
from accounts.models.custome_user import User
from branches.models.branch import Branch

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE,null = True,blank = True)   # one branch one manager
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email
