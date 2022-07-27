from django.db import models

# Create your models here.
class Registered(models.Model):
    userName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,primary_key=True)
    passWord = models.CharField(max_length=50)