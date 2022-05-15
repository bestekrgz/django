
from django.db.models.signals import *
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        subject = 'Welcome to YourTurn'
        message = 'Thank you for signing up for YourTurn. We hope you enjoy using it.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
        )


def update_profile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# @receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=Profile)
post_delete.connect(delete_profile, sender=Profile)
