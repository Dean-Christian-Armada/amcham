# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0021_auto_20150726_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='altrepresentative',
            name='full_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='execrepresentative',
            name='full_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
