from multiprocessing import AuthenticationError
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class post(models.Model):
    title= models.CharField(max_length=200)
    text= models.TextField(max_length=3000)
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Created_date= models.DateTimeField
    Published_date= models.DateTimeField


    def __str__(self) -> str:
        return self.title

class tpost(models.Model):
    title= models.CharField(max_length=200)
    text= models.TextField(max_length=3000)
    Created_date= models.DateTimeField
    Published_date= models.DateTimeField
    

    def __str__(self) -> str:
        return self.title