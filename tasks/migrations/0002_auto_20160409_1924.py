# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 4, 9, 19, 24, 9, 722806)),
        ),
    ]
