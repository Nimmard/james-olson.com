# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=100),), ('slug', models.SlugField(max_length=100),)],
            bases = (models.Model,),
            options = {u'verbose_name_plural': 'Categories'},
            name = 'Category',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=100),), ('slug', models.SlugField(max_length=100),), ('content', models.TextField(),), ('status', models.SmallIntegerField(default=2, choices=((1, 'Hidden',), (2, 'Draft',), (3, 'Published',),)),), ('featured', models.BooleanField(default=False),), ('category', models.ForeignKey(to=u'blog.Category', to_field=u'id'),), ('created', models.DateTimeField(auto_now_add=True),), ('updated_at', models.DateTimeField(auto_now=True),)],
            bases = (models.Model,),
            options = {u'ordering': ['featured', '-created'], u'verbose_name': 'Entry', u'verbose_name_plural': 'Entries'},
            name = 'Entries',
        ),
    ]
