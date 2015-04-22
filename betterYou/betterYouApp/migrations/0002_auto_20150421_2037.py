# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('betterYouApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 20, 37, 45, 62346), blank=True),
        ),
    ]
