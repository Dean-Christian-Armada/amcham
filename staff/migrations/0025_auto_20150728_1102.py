# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0024_auto_20150728_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
