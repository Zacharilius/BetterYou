from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	# Links UserProfiel to User model
	user = models.OneToOneField(User)

	# Add to the user profile
	picture = models.ImageField(upload_to="profile_images", blank=True)

	def __unicode__(self):
		return self.user.username

