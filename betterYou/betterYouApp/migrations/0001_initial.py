# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('numberChallenges', models.IntegerField(default=1)),
                ('postTime', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 20, 37, 6, 107555), blank=True)),
                ('votes', models.IntegerField(default=1)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['-postTime'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to=b'media/profile_images/', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(to='betterYouApp.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='userCompleteChallenge',
            field=models.ManyToManyField(related_name=b'user_complete_challenge', to='betterYouApp.UserProfile', blank=True),
            preserve_default=True,
        ),
    ]
