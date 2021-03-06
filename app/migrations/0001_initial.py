# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-05 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 6, 1, 55, 48, 224350), verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пост',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
