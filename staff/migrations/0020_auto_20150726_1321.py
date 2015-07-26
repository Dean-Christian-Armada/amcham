# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_company_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(default=None, unique=True, max_length=100),
        ),
    ]
