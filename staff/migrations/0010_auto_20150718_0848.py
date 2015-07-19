# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20150718_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='exec_representative',
            field=models.ForeignKey(default=None, to='staff.ExecRepresentative'),
        ),
        migrations.AlterField(
            model_name='member',
            name='alt_representative',
            field=models.ForeignKey(default=None, to='staff.AltRepresentative'),
        ),
    ]
