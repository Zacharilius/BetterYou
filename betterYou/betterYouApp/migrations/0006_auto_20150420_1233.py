# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('betterYouApp', '0005_auto_20150420_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='postTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 12, 33, 15, 414073), blank=True),
        ),
    ]
