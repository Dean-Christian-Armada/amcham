# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20150718_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='altrepresentative',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='execrepresentative',
            name='middle_name',
        ),
    ]
