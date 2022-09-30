from django.db import models
from django.contrib.auth.models import AbstractUser
from ..utils.models import UUIDModel


class User(UUIDModel, AbstractUser):

    username = models.CharField(max_length=10,primary_key=False, null=True, blank=True)

    email = models.EmailField(
        max_length=60,
        unique=True,
        help_text= 'Gmail or Privateemail'
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
