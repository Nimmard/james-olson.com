from django.db import models

# Create your models here.

#class Github(models.Models):

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message= models.TextField()
    date = models.DateField(auto_now=True)

