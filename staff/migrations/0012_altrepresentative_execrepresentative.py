# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20150725_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltRepresentative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('telephone', models.CharField(default=None, max_length=50)),
                ('mobile', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExecRepresentative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('telephone', models.CharField(default=None, max_length=50)),
                ('mobile', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
