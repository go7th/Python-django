# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('slug', models.CharField(verbose_name='网址', max_length=256, db_index=True)),
                ('content', models.TextField(verbose_name='内容', blank=True, default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('author', models.ForeignKey(verbose_name='作者', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '教程',
                'verbose_name_plural': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(verbose_name='栏目网址', max_length=256, db_index=True)),
                ('intro', models.TextField(verbose_name='栏目简介', default='')),
            ],
            options={
                'verbose_name': '栏目',
                'verbose_name_plural': '栏目',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(verbose_name='归属栏目', to='news.Column'),
        ),
    ]
