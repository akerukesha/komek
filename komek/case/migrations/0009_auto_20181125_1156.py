# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-11-25 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0008_auto_20181125_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='datetime',
            field=models.CharField(max_length=100, verbose_name='Time of gathering'),
        ),
    ]