# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=50, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postal_Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postal_code', models.CharField(max_length=5, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.CharField(max_length=50, unique=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(to='staff.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='postal_code',
            field=models.ForeignKey(to='staff.Postal_Code'),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.ForeignKey(to='staff.State'),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.ForeignKey(to='staff.Website'),
        ),
    ]
