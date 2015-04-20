from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import slugify
from django.utils import timezone

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
	user = models.ForeignKey(UserProfile, blank = False)
	title = models.CharField(max_length=128)
	numberChallenges = models.IntegerField(default=1)
	postTime = models.DateTimeField(default=timezone.now(), blank=True)
	votes = models.IntegerField(default=1)
	slug = models.SlugField(max_length=50)

	def get_absolute_url(self):
		return "/projects/better-you/%s/" % (self.slug)

	def save(self, *args, **kwargs):
		self.slug=slugify(self.title)
		try:
			super(Challenge, self).save(*args, **kwargs)
		except IntegrityError:
			print "An error occurred"

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-postTime']