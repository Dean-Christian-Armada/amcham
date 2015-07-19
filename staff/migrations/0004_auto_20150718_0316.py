# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_altrepresentative_company_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='alt_representative',
            field=models.ForeignKey(default=None, to='staff.AltRepresentative'),
        ),
        migrations.AddField(
            model_name='member',
            name='company',
            field=models.ForeignKey(default=None, to='staff.Company'),
        ),
    ]
