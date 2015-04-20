from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

from betterYouApp.forms import UserForm, UserProfileForm
from betterYouApp.models import Challenge

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
	return render(request, 'betterYouApp/profile.html', context_dict)

@login_required
def ranking(request):
	context_dict = {'nav_ranking': 'active'}
	return render(request, 'betterYouApp/ranking.html', context_dict)

@login_required
def propose(request):
	context_dict = {'nav_propose': 'active'}
	return render(request, 'betterYouApp/propose.html', context_dict)

@login_required
def vote(request):
	# Context dictionary used to pass variables. 
	context_dict = {'nav_vote': 'active'}

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

	return render(request, 'betterYouApp/vote.html', context_dict)

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
	
#@login_required
class ChallengeListView(ListView):
	def get_context_data(self, **kwargs):
		context_dict = super(ChallengeListView, self).get_context_data(**kwargs)
		context_dict['nav_vote'] = 'active'
		return context_dict

#def vote(request):
#	context_dict = {'nav_vote': 'active'}
#	return render(request, 'betterYou/vote.html', context_dict)