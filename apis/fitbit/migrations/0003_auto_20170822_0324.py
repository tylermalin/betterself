# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 03:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitbit', '0002_data_migrations_for_fitbit_types'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fitbittimeseriesdata',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='fitbittimeseriesdata',
            name='resource_type',
        ),
        migrations.RemoveField(
            model_name='fitbittimeseriesdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='FitbitTimeSeriesDataType',
        ),
        migrations.DeleteModel(
            name='FitbitTimeSeriesData',
        ),
    ]
