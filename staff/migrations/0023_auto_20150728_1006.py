# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0022_auto_20150728_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='company',
            field=models.ForeignKey(default=None, to='staff.Company'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(default=None, max_length=50, unique=True, null=True, blank=True),
        ),
    ]
