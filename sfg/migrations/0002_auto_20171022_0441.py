# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 04:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sfgmember',
            options={'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
    ]
