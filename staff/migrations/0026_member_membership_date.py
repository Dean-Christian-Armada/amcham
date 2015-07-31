# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0025_auto_20150728_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='membership_date',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
