# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-03 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
