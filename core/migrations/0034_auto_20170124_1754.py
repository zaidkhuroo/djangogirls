# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 17:54
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20170124_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_page_live',
            field=models.BooleanField(default=False, verbose_name='Website is ready'),
        ),
    ]
