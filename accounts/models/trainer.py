from django.db import models
from django.utils import timezone
from accounts.models.custome_user import User
from branches.models.branch import Branch
from django.core.exceptions import ValidationError

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null = True,blank = True)
    address = models.TextField(null= True,blank = True)
    created_at = models.DateTimeField(default=timezone.now)



    def clean(self):
        if not self.pk:  #new primary add hole,,count hobe
            trainer_count = Trainer.objects.filter(branch = self.branch).count()
            if trainer_count >=3:
                raise ValidationError(f"{self.branch.name} branch already has 3 trainers.")
            
    def save(self, *args, **kwargs):
        self.full_clean()   #validation check
        super().save(*args, **kwargs) # save

    def __str__(self):
        return self.user.email
