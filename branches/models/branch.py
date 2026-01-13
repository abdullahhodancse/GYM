from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length= 100,unique = True)
    address =  models.TextField()
    phone_number = models.CharField(max_length = 15,unique = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name