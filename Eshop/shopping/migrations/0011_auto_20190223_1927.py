# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-23 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_auto_20190222_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='imagePath',
            field=models.ImageField(blank=True, default='', upload_to='upload'),
        ),
    ]