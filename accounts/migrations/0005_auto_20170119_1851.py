# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170119_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fotografia',
            field=models.ImageField(blank=True, default='static/userDefault.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
