# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_news', '0004_article_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
