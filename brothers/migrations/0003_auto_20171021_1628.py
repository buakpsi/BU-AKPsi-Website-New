# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0002_eboardmember'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eboardmember',
            options={'verbose_name': 'Executive Board Member', 'verbose_name_plural': 'Executive Board Members'},
        ),
    ]