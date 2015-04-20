# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('betterYouApp', '0004_auto_20150420_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 12, 31, 7, 883445), blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(to='betterYouApp.UserProfile'),
        ),
    ]
