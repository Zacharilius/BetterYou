# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('betterYouApp', '0006_auto_20150420_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 13, 3, 42, 171351), blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='slug',
            field=models.SlugField(),
        ),
    ]
