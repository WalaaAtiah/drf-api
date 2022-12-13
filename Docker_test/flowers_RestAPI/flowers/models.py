from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Flower(models.Model):
    name=models.CharField(max_length=255)
    Sun_Needs=models.CharField(max_length=255)
    Soil_Needs=models.CharField(max_length=255)
    Zones=models.CharField(max_length=255)
    Height=models.CharField(max_length=255)
    Blooms_in=models.CharField(max_length=255)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    image=models.TextField(blank=True)
    def __str__(self):
        return self.name