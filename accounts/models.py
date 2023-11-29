from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=30, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)