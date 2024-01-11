from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.username
