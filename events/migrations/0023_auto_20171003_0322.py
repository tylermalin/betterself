# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_supplement_reminder_additions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplementreminder',
            options={'verbose_name': 'Supplement Reminder', 'verbose_name_plural': 'Supplement Reminders'},
        ),
        migrations.AlterField(
            model_name='dailyproductivitylog',
            name='source',
            field=models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sleepactivity',
            name='source',
            field=models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], max_length=50),
        ),
        migrations.AlterField(
            model_name='supplementevent',
            name='source',
            field=models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], default='web', max_length=50),
        ),
        migrations.AlterField(
            model_name='supplementreminder',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='useractivityevent',
            name='source',
            field=models.CharField(choices=[('api', 'Api'), ('ios', 'Ios'), ('android', 'Android'), ('web', 'Web'), ('user_excel', 'User_Excel'), ('text_message', 'Text_Message')], default='web', max_length=50),
        ),
    ]