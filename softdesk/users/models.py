from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'password2', 'first_name', 'last_name']

    objects = UserManager()
