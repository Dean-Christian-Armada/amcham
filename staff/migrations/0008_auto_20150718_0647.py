# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20150718_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecRepresentative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('telephone', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='altrepresentative',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='altrepresentative',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='altrepresentative',
            name='middle_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='altrepresentative',
            name='mobile',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='altrepresentative',
            name='telephone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='membership_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='referred_by',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
