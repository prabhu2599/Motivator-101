from django.db import models
import json


# Create your models here.

class AstroModel(models.Model):
    prediction = models.CharField(max_length=200)

    def __str__(self):
        return self.prediction
