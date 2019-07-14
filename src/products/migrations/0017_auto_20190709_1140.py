# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-09 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20190709_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_digital',
        ),
        migrations.AddField(
            model_name='product',
            name='bandwidth',
            field=models.IntegerField(default=1),
        ),
    ]