from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='user/avatars/', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
