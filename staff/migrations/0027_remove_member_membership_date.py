# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0026_member_membership_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='membership_date',
        ),
    ]
