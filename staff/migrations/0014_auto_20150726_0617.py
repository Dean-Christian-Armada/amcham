# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_auto_20150726_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodtype',
            name='blood_type',
            field=models.CharField(default=None, unique=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(default=None, unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(default=None, unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(default=None, unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(default=None, unique=True, max_length=100),
        ),
    ]
