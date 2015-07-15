# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20150712_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postal_code',
            name='postal_code',
            field=models.IntegerField(unique=True, null=True),
        ),
    ]
