# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0015_gender_membershipdate_nationality_position_postalcode_referredby_state_suffix_usaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, unique=True, max_length=50)),
                ('middle_name', models.CharField(default=None, unique=True, max_length=50)),
                ('last_name', models.CharField(default=None, unique=True, max_length=50)),
            ],
        ),
    ]
