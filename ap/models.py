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

class departments(models.Model):
    depname=models.CharField(max_length=20) 
    ndoctors=models.IntegerField()   

class doctable(models.Model):
    name=models.CharField(max_length=10)
    age=models.CharField(max_length=19)
    departments=models.CharField(max_length=20)

class logintb(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    utype=models.CharField(max_length=12)
    status=models.CharField(max_length=10)

