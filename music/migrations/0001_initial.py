# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=270)),
                ('year', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=290)),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=20)),
                ('album', models.ForeignKey(to='music.Albums')),
            ],
        ),
    ]
