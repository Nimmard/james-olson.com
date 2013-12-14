from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)

class Photo(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    caption = models.CharField(max_length=150)
    album = models.ForeignKey(Album, blank=True, null=True)


