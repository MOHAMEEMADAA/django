from django.db import models

# Create your models here.

class Account(models.Model):
    userName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    traineeObject = models.ForeignKey("trainee.Trainee", on_delete=models.CASCADE)
