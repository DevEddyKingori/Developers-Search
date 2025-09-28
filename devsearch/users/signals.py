from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from .tasks import create_profile_task, send_welcome_email_task


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        create_profile_task.delay(user.id)     # background profile creation
        send_welcome_email_task.delay(user.email)  # background email


def updateUser(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        user.first_name = instance.name
        user.username = instance.username
        user.email = instance.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        instance.user.delete()
    except Exception:
        pass
    print("Deleting user...")


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
