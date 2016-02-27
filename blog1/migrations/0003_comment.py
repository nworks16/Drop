# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_auto_20160101_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentauthor', models.CharField(max_length=50)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_body', models.TextField()),
            ],
        ),
    ]