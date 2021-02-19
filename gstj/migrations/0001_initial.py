# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-02-18 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('recordid', models.AutoField(primary_key=True, serialize=False, verbose_name=b'\xe8\xae\xb0\xe5\xbd\x95\xe5\x8f\xb7')),
                ('type', models.CharField(max_length=50L, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('taskid', models.CharField(max_length=50L, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=50L, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe4\xba\xba')),
                ('usedtime', models.FloatField(default=0, verbose_name=b'\xe8\x80\x97\xe6\x97\xb6')),
                ('status', models.CharField(max_length=50L, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('project', models.CharField(max_length=50L, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe9\xa1\xb9\xe7\x9b\xae')),
                ('link', models.CharField(max_length=500L, verbose_name=b'\xe6\x96\x87\xe6\xa1\xa3\xe9\x93\xbe\xe6\x8e\xa5')),
                ('detail', models.CharField(max_length=500L, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'db_table': 'gstj_record',
                'verbose_name': '\u5de5\u65f6\u8bb0\u5f55',
                'verbose_name_plural': '\u5de5\u65f6\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerid', models.CharField(max_length=50L, verbose_name=b'\xe5\xb7\xa5\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=50L, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('group', models.CharField(max_length=50L, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('location', models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50L, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba')),
                ('title', models.CharField(default=b'\xe5\x88\x9d\xe7\xba\xa7\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xb8\x88', max_length=50L, verbose_name=b'\xe8\x81\x8c\xe7\xba\xa7')),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'db_table': 'gstj_worker',
                'verbose_name': '\u5458\u5de5\u8868',
                'verbose_name_plural': '\u5458\u5de5\u8868',
            },
        ),
    ]