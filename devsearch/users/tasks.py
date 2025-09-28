from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile


@shared_task
def create_profile_task(user_id):
    user = User.objects.get(id=user_id)
    Profile.objects.create(
        user=user,
        username=user.username,
        email=user.email,
        name=user.first_name
    )
    return f"Profile created for {user.username}"


@shared_task
def send_welcome_email_task(email):
    subject = "Welcome to Devsearch!"
    message = "We are glad you are here!"

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return f"Email sent to {email}"
