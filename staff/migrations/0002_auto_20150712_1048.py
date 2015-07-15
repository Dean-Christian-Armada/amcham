# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postal_code',
            name='postal_code',
            field=models.IntegerField(max_length=10, unique=True, null=True),
        ),
    ]
