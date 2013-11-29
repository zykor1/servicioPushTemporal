from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('push.urls')),
    url(r'^$', 'testPush.views.indexTest'),
    url(r'^enviaNotificacion$', 'testPush.views.enviaNotificacion'),
    url(r'^leeMensajes$', 'testPush.views.leeMensajes'),
)

# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
