from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message= models.TextField()
    date = models.DateField(auto_now=True)

class Commits(models.Model):
    date = models.DateTimeField()
    title = models.TextField()
    code = models.TextField()
    summary = models.TextField()
