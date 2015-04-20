from django.conf.urls import patterns, include, url
from django.contrib import admin
from betterYouApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'betterYou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^projects/better-you/', include('betterYouApp.urls')),

)
