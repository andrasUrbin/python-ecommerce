# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-28 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=29.99, max_digits=10),
        ),
    ]
