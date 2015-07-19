# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='Nationality',
        ),
        migrations.RemoveField(
            model_name='company',
            name='USCity',
        ),
        migrations.RemoveField(
            model_name='company',
            name='USState',
        ),
        migrations.RemoveField(
            model_name='company',
            name='USZip',
        ),
        migrations.RemoveField(
            model_name='company',
            name='city',
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='company',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='company',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='company',
            name='state',
        ),
        migrations.RemoveField(
            model_name='company',
            name='tin',
        ),
        migrations.RemoveField(
            model_name='company',
            name='website',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Fax',
        ),
        migrations.DeleteModel(
            name='Mobile',
        ),
        migrations.DeleteModel(
            name='Nationality',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.DeleteModel(
            name='Postal_Code',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Tin',
        ),
        migrations.DeleteModel(
            name='USCity',
        ),
        migrations.DeleteModel(
            name='USState',
        ),
        migrations.DeleteModel(
            name='USZip',
        ),
        migrations.DeleteModel(
            name='Website',
        ),
    ]
