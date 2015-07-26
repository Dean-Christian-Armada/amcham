# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_member'),
    ]

    operations = [
        migrations.DeleteModel(
            name='USAddress',
        ),
        migrations.AlterField(
            model_name='membershipdate',
            name='membership_date',
            field=models.DateField(unique=True),
        ),
    ]
