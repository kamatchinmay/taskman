# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20160706_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='DOB',
            field=models.DateField(verbose_name='Date of Birth / Registration'),
        ),
    ]