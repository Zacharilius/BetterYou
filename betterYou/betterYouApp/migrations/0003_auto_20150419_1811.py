# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('betterYouApp', '0002_auto_20150419_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('numberChallenges', models.IntegerField(default=1)),
                ('postTime', models.DateTimeField(default=datetime.datetime(2015, 4, 19, 18, 11, 23, 464230), blank=True)),
                ('votes', models.IntegerField(default=1)),
                ('slug', models.SlugField(unique=True, max_length=40)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['postTime'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='createchallenge',
            name='user',
        ),
        migrations.DeleteModel(
            name='CreateChallenge',
        ),
    ]
