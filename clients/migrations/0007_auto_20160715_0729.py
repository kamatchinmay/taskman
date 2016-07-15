# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20160710_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='_my_subclass',
            field=models.CharField(default='individual', max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='PIN',
            field=models.CharField(help_text='Mandatory', max_length=6, verbose_name='PIN Code'),
        ),
    ]
