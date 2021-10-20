from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default="India")
    is_admin = models.BooleanField(default=False),
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
