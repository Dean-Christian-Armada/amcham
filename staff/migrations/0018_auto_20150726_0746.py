# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_auto_20150726_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='annual_revenue',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ForeignKey(default=None, to='staff.City'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(default=1, to='staff.Country'),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='postal_code',
            field=models.ForeignKey(default=None, to='staff.PostalCode'),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.ForeignKey(default=2, to='staff.State'),
        ),
        migrations.AddField(
            model_name='company',
            name='street_1',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='street_2',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='tin',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='us_address_1',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='us_address_2',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='us_city',
            field=models.ForeignKey(related_name='us_city', default=None, to='staff.City'),
        ),
        migrations.AddField(
            model_name='company',
            name='us_state',
            field=models.ForeignKey(related_name='us_state', default=None, to='staff.State'),
        ),
        migrations.AddField(
            model_name='company',
            name='us_zip',
            field=models.ForeignKey(related_name='us_zip', default=None, to='staff.PostalCode'),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
