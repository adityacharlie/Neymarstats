# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0002_auto_20151120_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='keywords',
            field=models.CharField(max_length=100, null=True, verbose_name='keywords'),
        ),
    ]
