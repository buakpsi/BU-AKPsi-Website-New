# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-18 02:19
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0003_auto_20180118_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushprofile',
            name='events_attended',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=list, size=None),
        ),
    ]