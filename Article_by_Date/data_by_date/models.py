# models.py

from django.db import models

class article(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Display the name in the admin interface or when printing the object



