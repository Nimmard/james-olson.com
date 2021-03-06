# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=255),), ('email', models.EmailField(max_length=75),), ('message', models.TextField(),), ('date', models.DateField(auto_now=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Contact',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('date', models.DateTimeField(),), ('title', models.CharField(max_length=255),), ('code', models.CharField(max_length=255),), ('summary', models.TextField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Commits',
        ),
    ]
