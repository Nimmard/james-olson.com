# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=100),)],
            bases = (models.Model,),
            options = {},
            name = 'Album',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('image', models.ImageField(upload_to='images/%Y/%m/%d'),), ('caption', models.CharField(max_length=150),), ('album', models.ForeignKey(to=u'uploads.Album', to_field=u'id', null=True, blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Photo',
        ),
    ]
