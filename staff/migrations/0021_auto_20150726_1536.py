# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_auto_20150726_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='member',
            name='blood_type',
            field=models.ForeignKey(default=None, to='staff.BloodType'),
        ),
        migrations.AddField(
            model_name='member',
            name='citizenship',
            field=models.ForeignKey(default=1, to='staff.Nationality'),
        ),
        migrations.AddField(
            model_name='member',
            name='company_email',
            field=models.ForeignKey(related_name='company_email', default=None, to='staff.Email'),
        ),
        migrations.AddField(
            model_name='member',
            name='fax',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.ForeignKey(default=1, to='staff.Gender'),
        ),
        migrations.AddField(
            model_name='member',
            name='mobile',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='personal_email',
            field=models.ForeignKey(default=None, to='staff.Email'),
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.ForeignKey(default=None, to='staff.Position'),
        ),
        migrations.AddField(
            model_name='member',
            name='suffix',
            field=models.ForeignKey(default=None, to='staff.Suffix'),
        ),
        migrations.AddField(
            model_name='member',
            name='telephone',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='middle_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
