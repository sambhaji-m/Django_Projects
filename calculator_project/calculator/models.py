from django.db import models

# Create your models here.

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
