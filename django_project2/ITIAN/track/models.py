from django.db import models

# Create your models here.

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    trackName = models.CharField(max_length=255)