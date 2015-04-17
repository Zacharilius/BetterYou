from django.conf.urls import patterns, url
from betterYouApp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^ranking/$', views.ranking, name='ranking'),
	url(r'^vote/$', views.vote, name='vote'),
	url(r'^sign-up/$', views.user_signup, name='user_signup'),
	url(r'^log-in/$', views.user_login, name='user_login'),
	url(r'^restricted/$', views.restricted, name='restricted'),
	url(r'^logout/$, views.user_logout, name='logout'),
)
