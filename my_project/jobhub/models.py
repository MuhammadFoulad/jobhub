from django.db import models

# Create your models here.

class Login(models.Model):
    email=models.CharField(max_length=255)
    phone=models.IntegerField(default=0)
    password=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    salt=models.CharField(max_length=255)

class Users(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.IntegerField(default=0)
    password=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    login=models.ForeignKey(Login,default=1,on_delete=models.CASCADE,)


    
