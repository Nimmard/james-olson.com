from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return "/blog/category/{0}".format(self.slug)

    class Meta:
        verbose_name_plural = "Categories"

class Entries(models.Model):
    HIDDEN = 1
    DRAFT = 2
    PUBLISHED = 3

    STATUS_CHOICES = (
            (HIDDEN, "Hidden"),
            (DRAFT, "Draft"),
            (PUBLISHED, "Published"),
            )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    status = models.SmallIntegerField(default=DRAFT, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['featured', '-created']
        verbose_name_plural="Entries"
        verbose_name = "Entry"

    def get_absolute_url(self):
        return "/blog/{0}/".format(self.slug)



