# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 15:09
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0005_remove_rushapplication_application_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='rushapplication',
            name='application_answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None),
            preserve_default=False,
        ),
    ]