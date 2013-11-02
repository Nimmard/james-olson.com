# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('main', '0002_auto')]

    operations = [
        migrations.AlterField(
            field = models.TextField(),
            name = 'title',
            model_name = 'commits',
        ),
    ]
