# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20170212_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='aisles',
        ),
        migrations.AddField(
            model_name='store',
            name='aisles',
            field=models.ManyToManyField(blank=True, null=True, to='login.Aisle'),
        ),
    ]
