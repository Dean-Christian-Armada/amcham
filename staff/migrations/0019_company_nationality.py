# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0018_auto_20150726_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='nationality',
            field=models.ForeignKey(default=1, to='staff.Nationality'),
        ),
    ]
