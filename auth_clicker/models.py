from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserData(models.Model):
    user = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
