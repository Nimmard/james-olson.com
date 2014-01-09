# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('uploads', '0001_initial')]

    operations = [
        migrations.AddField(
            field = models.CharField(default='blah', max_length=30),
            name = 'name',
            model_name = 'photo',
        ),
    ]
