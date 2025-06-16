from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=21)
    summary = models.textField(max_length=2000)