from datetime import datetime
from django.db import models

# Create your models here.


class Elephant(models.Model):
    event = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=32)
    lon = models.CharField(max_length=32)
    lat = models.CharField(max_length=32)
    datetime = models.DateTimeField()


class Whale(models.Model):
    event = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=32)
    lon = models.CharField(max_length=32)
    lat = models.CharField(max_length=32)
    datetime = models.DateTimeField()


class Upload_data(models.Model):
    event = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=32)
    lon = models.CharField(max_length=32)
    lat = models.CharField(max_length=32)
    datetime = models.DateTimeField()
