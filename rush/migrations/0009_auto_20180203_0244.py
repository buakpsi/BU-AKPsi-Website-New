# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-03 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0008_merge_20180202_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushapplication',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
