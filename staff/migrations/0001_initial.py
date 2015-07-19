# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('membership_date', models.DateField(default=None)),
                ('street_1', models.CharField(max_length=200, null=True, blank=True)),
                ('street_2', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=50, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fax', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=50, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nationality', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postal_Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postal_code', models.IntegerField(unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tin', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='USCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('us_city', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='USState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('us_state', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='USZip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('us_zip', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(unique=True, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='Nationality',
            field=models.ForeignKey(default=None, to='staff.Nationality'),
        ),
        migrations.AddField(
            model_name='company',
            name='USCity',
            field=models.ForeignKey(default=None, to='staff.USCity'),
        ),
        migrations.AddField(
            model_name='company',
            name='USState',
            field=models.ForeignKey(default=None, to='staff.USState'),
        ),
        migrations.AddField(
            model_name='company',
            name='USZip',
            field=models.ForeignKey(default=None, to='staff.USZip'),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ForeignKey(default=None, to='staff.City'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(default=None, to='staff.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.ForeignKey(default=None, to='staff.Email'),
        ),
        migrations.AddField(
            model_name='company',
            name='fax',
            field=models.ForeignKey(default=None, to='staff.Fax'),
        ),
        migrations.AddField(
            model_name='company',
            name='mobile',
            field=models.ForeignKey(default=None, to='staff.Mobile'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.ForeignKey(default=None, to='staff.Phone'),
        ),
        migrations.AddField(
            model_name='company',
            name='postal_code',
            field=models.ForeignKey(default=None, to='staff.Postal_Code'),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.ForeignKey(to='staff.State'),
        ),
        migrations.AddField(
            model_name='company',
            name='tin',
            field=models.ForeignKey(default=None, to='staff.Tin'),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.ForeignKey(default=None, to='staff.Website'),
        ),
    ]
