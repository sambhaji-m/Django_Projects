from django.db import models

# Create your models here.

class enquiry(models.Model):
    name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.subject_type

 