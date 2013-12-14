# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('main', '0004_contact_phone')]

    operations = [
        migrations.AlterField(
            field = models.CharField(max_length=20),
            name = 'phone',
            model_name = 'contact',
        ),
    ]
