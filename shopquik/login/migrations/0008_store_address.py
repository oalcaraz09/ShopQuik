# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170212_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
