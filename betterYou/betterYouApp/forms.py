from django import forms
from django.contrib.auth.models import User
from betterYouApp.models import UserProfile, Challenge

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)

class CreateChallenge(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Read a book")
	numberChallenges = forms.IntegerField(max_value = 30, min_value=1, help_text = "Number of times challenge must be completed during the week")
	#Add hidden user input
	#Fix slugify in model

	class Meta:
		model = Challenge
		exclude = ('user', 'postTime', 'votes', 'slug')
