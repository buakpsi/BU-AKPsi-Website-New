# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-19 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0006_merge_20180118_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='minor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='brother',
            name='minor_school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
