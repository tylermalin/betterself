# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-01 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_auto_20161224_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]