# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 21:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill_match', '0004_auto_20160401_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='availability',
        ),
    ]