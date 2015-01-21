from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
#from contacts.views import twitter_login, twitter_logout, twitter_authenticated

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^contacts/', include('contacts.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'auth/', include('social_auth.urls')),
#	url(r'^login/?$', twitter_login),
#	url(r'^logout/?$', twitter_logout),
#	url(r'^login/authenticated/?$', twitter_authenticated),
)

