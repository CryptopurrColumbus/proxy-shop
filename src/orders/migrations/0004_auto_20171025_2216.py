# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20170929_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True,
                                       default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
