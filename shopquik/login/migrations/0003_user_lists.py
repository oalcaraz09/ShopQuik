# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-12 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170212_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lists',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.List'),
        ),
    ]