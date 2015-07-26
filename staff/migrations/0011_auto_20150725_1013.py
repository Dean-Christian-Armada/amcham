# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_auto_20150718_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='alt_representative',
        ),
        migrations.RemoveField(
            model_name='member',
            name='company',
        ),
        migrations.RemoveField(
            model_name='member',
            name='exec_representative',
        ),
        migrations.DeleteModel(
            name='AltRepresentative',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='ExecRepresentative',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
