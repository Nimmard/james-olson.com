# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('uploads', '0002_photo_name')]

    operations = [
        migrations.AlterField(
            field = models.CharField(max_length=30, null=True, blank=True),
            name = 'name',
            model_name = 'photo',
        ),
    ]
