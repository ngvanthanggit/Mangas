from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, blank=False)
    avatar = models.ImageField(null=True)
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username