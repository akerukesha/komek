# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-11-24 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20181124_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='timestamp',
            field=models.BigIntegerField(default=1543058697550, verbose_name='Department timestamp'),
        ),
    ]