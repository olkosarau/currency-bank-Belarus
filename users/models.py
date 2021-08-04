from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
       return "{} -{}".format(self.username, self.email)