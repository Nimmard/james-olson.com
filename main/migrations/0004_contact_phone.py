# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('main', '0003_auto')]

    operations = [
        migrations.AddField(
            field = models.CharField(default=-8700, max_length=20),
            name = 'phone',
            model_name = 'contact',
        ),
    ]
