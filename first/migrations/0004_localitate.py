# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20160616_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localitate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
            ],
        ),
    ]