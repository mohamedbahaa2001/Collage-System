from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    


class Register(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()