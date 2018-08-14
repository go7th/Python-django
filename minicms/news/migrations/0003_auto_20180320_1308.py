# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180319_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(verbose_name='首页显示', default=False),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(verbose_name='导航显示', default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(verbose_name='网址', max_length=256, unique=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='intro',
            field=DjangoUeditor.models.UEditorField(verbose_name='栏目简介内容', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(verbose_name='栏目网址', max_length=256, unique=True, db_index=True),
        ),
    ]
