# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-11-24 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20181124_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='datetime',
            field=models.BigIntegerField(default=1543058590161, verbose_name='Time of gathering'),
        ),
        migrations.AlterField(
            model_name='case',
            name='deadline',
            field=models.BigIntegerField(default=1543058590161, verbose_name='Deadline'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.BigIntegerField(default=1543058590160, verbose_name='Priority timestamp'),
        ),
        migrations.AlterField(
            model_name='priority',
            name='timestamp',
            field=models.BigIntegerField(default=1543058590160, verbose_name='Priority timestamp'),
        ),
    ]
