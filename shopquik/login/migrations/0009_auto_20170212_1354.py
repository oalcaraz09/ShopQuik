# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_store_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='aisles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Aisle'),
        ),
    ]
