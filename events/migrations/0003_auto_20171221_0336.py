# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 03:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_add_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplementlog',
            options={'ordering': ['user', '-time'], 'verbose_name': 'Supplement Log', 'verbose_name_plural': 'Supplement Logs'},
        ),
    ]