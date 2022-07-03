from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    phone_number = models.CharField(max_length=15, null=True, blank=True, default="", unique=True)
    email = models.EmailField(unique=True, default="")
    last_visit = models.DateTimeField(null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True, unique=True)
    REQUIRED_FIELDS = ['phone_number']
    
    def __str__(self):
        return f"{self.username}"