from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    username = models.CharField(unique=True, max_length=50)

    def __str__(self) -> str:
        return self.email
