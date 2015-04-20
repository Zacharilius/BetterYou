# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('betterYouApp', '0003_auto_20150419_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 12, 30, 3, 90856), blank=True),
        ),
    ]
