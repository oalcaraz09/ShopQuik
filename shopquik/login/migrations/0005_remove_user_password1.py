# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-12 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170212_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
    ]
