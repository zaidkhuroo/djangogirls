# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 14:53
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organize', '0002_auto_20170107_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventapplication',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventapplication',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
