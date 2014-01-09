from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)
    
    def get_first_image(self):
        return self.photo_set.all()[0].image

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    caption = models.CharField(max_length=150)
    album = models.ForeignKey(Album, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self):
        if not self.name:
            print self.image.name
            self.name = self.image.name
        super(Photo, self).save()
