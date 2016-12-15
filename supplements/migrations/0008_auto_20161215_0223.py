# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-15 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0007_auto_20161215_0222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set([('name', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='supplement',
            unique_together=set([('user', 'name', 'vendor')]),
        ),
    ]
