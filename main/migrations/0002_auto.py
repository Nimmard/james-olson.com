# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('main', '0001_initial')]

    operations = [
        migrations.AlterField(
            field = models.TextField(),
            name = 'code',
            model_name = 'commits',
        ),
    ]
