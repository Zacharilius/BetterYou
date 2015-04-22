from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from django.utils import timezone
from datetime import datetime, timedelta

from betterYouApp.forms import UserForm, UserProfileForm, CreateChallenge
from betterYouApp.models import Challenge, UserProfile

# Create your views here.
def index(request):
	context_dict = {'nav_home': 'active'}
	return render(request, 'betterYouApp/home.html',context_dict)

def about(request):
	context_dict = {'nav_about': 'active'}
	return render(request, 'betterYouApp/about.html', context_dict)

@login_required
def profile(request):
	context_dict = {'nav_profile': 'active'}

	# Fetches user profile that matches the username's id
	# Then pass the object to the context dictionary
	userProfile = UserProfile.objects.get(user=request.user)
	context_dict["userProfile"] = userProfile
	print userProfile
	print request.user

	# Fetches the most recent vote-challenges
	vote_challenges = Challenge.objects.filter(user=userProfile)[:5]
	context_dict["my_created_challenges"] = vote_challenges
	print vote_challenges
	
	# Fetches the most recent current-challenges
	current_challenges = Challenge.objects.filter(user=userProfile)[:5]
	context_dict["my_completed_challenges"] = current_challenges
	print current_challenges

	return render(request, 'betterYouApp/profile.html', context_dict)

@login_required
def ranking(request):
	context_dict = {'nav_ranking': 'active'}

	user_rankings = UserProfile.objects.all().order_by('-points');
	context_dict['user_rankings'] = user_rankings
	return render(request, 'betterYouApp/ranking.html', context_dict)

@login_required
def propose(request):
	# Context dictionary used to pass variables.
	accepted = False
 	context_dict = {'nav_propose': 'active'}

	# If HTTP POST
	if request.method == 'POST':
		form = CreateChallenge(request.POST)

		if form.is_valid():
			addedForm = form.save(commit=False)
			addedForm.user = UserProfile.objects.get(user=request.user)
			addedForm.save()
			accepted = True
		else:
			print form.errors
	# Return a new blank form
	form = CreateChallenge()
	context_dict['form'] = form
	context_dict['accepted'] = accepted
	return render(request, 'betterYouApp/propose.html', context_dict)

class VoteListView(ListView):
	template_name="betterYouApp/vote_list.html"
	def get_queryset(self):
		# Gets the current time
		endTime = timezone.now()
		# Gets the time from a week ago
		startTime = endTime - timedelta(days=7)
		try:
			challenges = Challenge.objects.all()
			# Only displays posts within last week
			return challenges.order_by('-votes').filter(postTime__range=[startTime, endTime])
		except Challenge.DoesNotExist:
			return Challenge.objects.none()

	def get_context_data(self, **kwargs):
		context_dict = super(VoteListView, self).get_context_data(**kwargs)
		context_dict['nav_vote'] = 'active'
		return context_dict

def user_signup(request):
	# Context dictionary used to pass variables. 
	context_dict = {'nav_signup': 'active'}

	#Initialized to false so template knows if registration was successful.
	# If sucessfully registers. Code chages to True with successful registration
	registered = False

	#Processes the data if it is a HTTP POST
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# Check if user forms are valid
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Hash the password
			user.set_password(user.password)
			user.save()

			# Gets the UserProfile instance
			# We set commit=False b/c I need to set user attribute 
			# For integrity reasons
			profile = profile_form.save(commit=False)
			profile.user = user

			# Checks if user provided a profile pic
			# Add to user profile model if they did
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			# Successfully registered so update registered to True
			registered = True

		else:
			print user_form.errors, profile_form.errors

	# If not HTTP POST then send form
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Pass in user_form, profile_form, and if the user has successfully registered
	context_dict['user_form'] = user_form
	context_dict['profile_form'] = profile_form
	context_dict['registered'] = registered

	return render(request, 'betterYouApp/signup.html', context_dict)

def user_login(request):
	# Context dictionary used to pass variables. 
	context_dict = {'nav_login': 'active'}

	# If HTTP POST
	if request.method == 'POST':
		# Grab the username and password
		username = request.POST.get('username')
		password = request.POST.get('password')

		# If a user exists, then authenticate returns a user object
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/projects/better-you/')
			else:
				return HttpResponse("Account disabled. Contact Support")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'betterYouApp/login.html', context_dict)

@login_required
def restricted(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/projects/better-you')
	
class ChallengeListView(ListView):
	template_name="betterYouApp/challenge_list.html"

	def get_queryset(self):
		# Gets the current time
		endTime = timezone.now()
		# Gets the time from a week ago
		startTime = endTime - timedelta(days=7)
		try:
			challenges = Challenge.objects.all()
			# Only displays posts within last week
			return challenges.order_by('postTime').filter(postTime__range=[startTime, endTime]).filter(votes__gt=9)
		except Challenge.DoesNotExist:
			return Challenge.objects.none()

	def get_context_data(self, **kwargs):
		context_dict = super(ChallengeListView, self).get_context_data(**kwargs)
		context_dict['nav_currentChallenges'] = 'active'
		return context_dict

@login_required
def like_challenge(request):
	challenge_id = None
	if request.method == 'GET':
		challenge_id = request.GET['challenge_id']
	votes = 0
	if challenge_id:
		challenge = Challenge.objects.get(id=int(challenge_id))
		print "challenge.user"
		print type(challenge.user)
		print "request.user"
		print type(request.user)
		if challenge:
			userRequest = UserProfile.objects.get(user=request.user)
			votes = challenge.votes
			if challenge.user == userRequest:
				pass
			else:
				votes = votes + 1
				challenge.votes = votes		
				challenge.save()
	return HttpResponse(votes)