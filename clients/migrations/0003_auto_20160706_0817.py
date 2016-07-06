# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20160706_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='CExNo',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Central Excise Regn. No.'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='STN',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Service Tax Regn. No.'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='TAN',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='TAN'),
        ),
    ]