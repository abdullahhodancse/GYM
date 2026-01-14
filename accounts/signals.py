from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from accounts.models.manager import Manager
from accounts.models.trainer import Trainer
from accounts.models.member import Member

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_on_registration(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.role == "manager":
        Manager.objects.create(user=instance)

    elif instance.role == "trainer":
        Trainer.objects.create(user=instance)

    elif instance.role == "member":
        Member.objects.create(user=instance)
