from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_blog_category', {'slug': self.slug })
    class Meta:
        verbose_name_plural = "Categories"

class Entries(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name_plural="Entries"
        verbose_name = "Entry"

    def get_absolute_url(self):
        return "/blog/{0}/".format(self.slug)



