# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20160706_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='PAN',
            field=models.CharField(help_text='PAN is mandatory', max_length=10, verbose_name='PAN'),
        ),
    ]
