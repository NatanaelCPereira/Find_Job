from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls import patterns, include, url

#from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('Site.views',
    # Examples:

    (r'^$', 'home'),
    (r'^usuario/add/', 'add_usuario'),
    (r'^usuario/(?P<id>\d+)/$', 'ver_usuario'),
    (r'^usuario/update/(?P<id>\d+)/', 'update_usuario'),
    (r'^usuario/delete/(?P<id>\d+)/', 'delete_usuario'),
)
