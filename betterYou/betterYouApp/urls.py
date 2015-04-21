from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from betterYouApp.models import Challenge
from betterYouApp.views import ChallengeListView, VoteListView
from betterYouApp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^ranking/$', views.ranking, name='ranking'),
	url(r'^propose-challenge/$', views.propose, name='propose'),
	url(r'^current-challenges/(?P<page>\d+)?/?$', login_required(ChallengeListView.as_view(
		paginate_by=5,
		model=Challenge,
		))),
	url(r'^vote-challenges/(?P<page>\d+)?/?$', login_required(VoteListView.as_view(
		paginate_by=5,
		model=Challenge,
		))),	
	url(r'^sign-up/$', views.user_signup, name='user_signup'),
	url(r'^log-in/$', views.user_login, name='user_login'),
	url(r'^restricted/$', views.restricted, name='restricted'),
	url(r'^log-out/$', views.user_logout, name='logout'),
	url(r'^like-challenge/$', views.like_challenge, name='like_challenge'),
)
