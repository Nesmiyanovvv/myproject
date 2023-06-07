from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1337)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)