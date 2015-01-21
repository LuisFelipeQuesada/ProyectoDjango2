from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Lista de url's que se utilizan en la aplicacion
urlpatterns = patterns('contacts.views',
    url(r'^login/$', 'login'),
    url(r'^disconnect/$', redirect_to, {'url':'login'}),
    url(r'^$', 'index'),
    url(r'^add/$', 'add'),
    url(r'^create/$', 'create'),
	url(r'^view/$', 'view'),
    url(r'^view/(?P<contact_id>\d+)/edit/$', 'edit'),
    url(r'^view/(?P<contact_id>\d+)/viewContact/$', 'viewContact'),
	url(r'auth/', include('social_auth.urls')),
	url (r'^view/(?P<contact_id>\d+)/delete', 'delete')
)


