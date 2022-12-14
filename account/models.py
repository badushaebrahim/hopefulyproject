from datetime import datetime
from enum import unique
from xmlrpc.client import ResponseError
from django.contrib.auth.models import AbstractUser
from django.db import models
from pytz import timezone
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def _create_user(self,  password, username=None, **extra_fields):
        user = self.model(username=username,  **extra_fields)
        
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def create_user(self, password=None, username=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username,  password, **extra_fields)

    def create_superuser(self, password, username=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser = True"))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff = True"))

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["first_name","email"]

    # username = None
    objects = CustomUserManager()

    def __str__(self):
        return self.first_name


