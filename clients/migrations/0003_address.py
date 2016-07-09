# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20160707_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Line1', models.CharField(help_text='Mandatory', max_length=30, verbose_name='Address Line 1')),
                ('Line2', models.CharField(help_text='Mandatory', max_length=30, verbose_name='Address Line 2')),
                ('State', models.CharField(choices=[('IN-GA', 'Goa'), ('IN-AP', 'Andhra Pradesh'), ('IN-AR', 'Arunachal Pradesh'), ('IN-AS', 'Assam'), ('IN-BR', 'Bihar'), ('IN-CT', 'Chhattisgarh'), ('IN-GJ', 'Gujarat'), ('IN-HR', 'Haryana'), ('IN-HP', 'Himachal Pradesh'), ('IN-JK', 'Jammu and Kashmir'), ('IN-JH', 'Jharkhand'), ('IN-KA', 'Karnataka'), ('IN-KL', 'Kerala'), ('IN-MP', 'Madhya Pradesh'), ('IN-MH', 'Maharashtra'), ('IN-MN', 'Manipur'), ('IN-ML', 'Meghalaya'), ('IN-MZ', 'Mizoram'), ('IN-NL', 'Nagaland'), ('IN-OR', 'Odisha'), ('IN-PB', 'Punjab'), ('IN-RJ', 'Rajasthan'), ('IN-SK', 'Sikkim'), ('IN-TN', 'Tamil Nadu'), ('IN-TG', 'Telangana'), ('IN-TR', 'Tripura'), ('IN-UT', 'Uttarakhand'), ('IN-UP', 'Uttar Pradesh'), ('IN-WB', 'West Bengal'), ('IN-AN', 'Andaman and Nicobar Islands'), ('IN-CH', 'Chandigarh'), ('IN-DN', 'Dadra and Nagar Haveli'), ('IN-DD', 'Daman and Diu'), ('IN-DL', 'Delhi'), ('IN-LD', 'Lakshadweep'), ('IN-PY', 'Puducherry')], default='IN-GA', help_text='Mandatory', max_length=5, verbose_name='State')),
                ('PIN', models.CharField(choices=[('IN-GA', 'Goa'), ('IN-AP', 'Andhra Pradesh'), ('IN-AR', 'Arunachal Pradesh'), ('IN-AS', 'Assam'), ('IN-BR', 'Bihar'), ('IN-CT', 'Chhattisgarh'), ('IN-GJ', 'Gujarat'), ('IN-HR', 'Haryana'), ('IN-HP', 'Himachal Pradesh'), ('IN-JK', 'Jammu and Kashmir'), ('IN-JH', 'Jharkhand'), ('IN-KA', 'Karnataka'), ('IN-KL', 'Kerala'), ('IN-MP', 'Madhya Pradesh'), ('IN-MH', 'Maharashtra'), ('IN-MN', 'Manipur'), ('IN-ML', 'Meghalaya'), ('IN-MZ', 'Mizoram'), ('IN-NL', 'Nagaland'), ('IN-OR', 'Odisha'), ('IN-PB', 'Punjab'), ('IN-RJ', 'Rajasthan'), ('IN-SK', 'Sikkim'), ('IN-TN', 'Tamil Nadu'), ('IN-TG', 'Telangana'), ('IN-TR', 'Tripura'), ('IN-UT', 'Uttarakhand'), ('IN-UP', 'Uttar Pradesh'), ('IN-WB', 'West Bengal'), ('IN-AN', 'Andaman and Nicobar Islands'), ('IN-CH', 'Chandigarh'), ('IN-DN', 'Dadra and Nagar Haveli'), ('IN-DD', 'Daman and Diu'), ('IN-DL', 'Delhi'), ('IN-LD', 'Lakshadweep'), ('IN-PY', 'Puducherry')], help_text='Mandatory', max_length=6, verbose_name='State')),
            ],
        ),
    ]