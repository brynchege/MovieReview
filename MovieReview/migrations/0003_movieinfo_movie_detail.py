# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-10 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0002_auto_20190310_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='movie_detail',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]