from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from django.contrib import auth


def create_profile(self, **kwargs):
    Profile.objects.create(
        user=self, **kwargs  # you can pass other fields values upon creating
    )


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to="profile_image", blank=True)


auth.models.User.add_to_class("create_profile", create_profile)
