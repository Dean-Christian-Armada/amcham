# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0023_auto_20150728_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.CharField(default=None, unique=True, max_length=100),
        ),
    ]
