# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='is_featured'),
        ),
        migrations.AddField(
            model_name='question',
            name='keywords',
            field=models.TextField(null=True, verbose_name='keywords', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='likecount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.IntegerField(default=1, verbose_name='question Type', choices=[(1, 'IDEA'), (2, 'CATALOGUE'), (3, 'PROJECT')]),
        ),
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=b'slug_text', verbose_name='slug', unique_for_date=b'pub_date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='question'),
        ),
    ]
