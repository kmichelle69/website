# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-23 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewRepairForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SAW', 'chainsaw'), ('MWR', 'lawnmower'), ('WTR', 'weedeater')], max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
            ],
        ),
    ]
