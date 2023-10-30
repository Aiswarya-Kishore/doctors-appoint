from django.db import models

# Create your models here.
class appointments(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    docter=models.CharField(max_length=10)
    departments=models.CharField(max_length=20)
    message=models.CharField(max_length=100)

