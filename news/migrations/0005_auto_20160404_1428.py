# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160404_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainnewslist',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='newsdetail',
            old_name='data',
            new_name='date',
        ),
    ]