from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import slugify

# Create your models here.
class UserProfile(models.Model):
	# Links UserProfiel to User model
	user = models.OneToOneField(User)
	points = models.IntegerField(default=0)

	# Add to the user profile
	picture = models.ImageField(upload_to="media/profile_images/", blank=True)

	def __unicode__(self):
		return self.user.username

class Challenge(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	numberChallenges = models.IntegerField(default=1)
	postTime = models.DateTimeField(default=datetime.now(), blank=True)
	votes = models.IntegerField(default=1)
	slug = models.SlugField(max_length=40, unique=True)

	def get_absolute_url(self):
		return "/projects/better-you/%s/" % (self.slug)

	def save(self, *args, **kwargs):
		self.slug=slugify(self.title)
		super(Challenge, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['postTime']