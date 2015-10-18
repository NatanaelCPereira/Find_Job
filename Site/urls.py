from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls import patterns, include, url

#from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('Site.views',
    # Examples:
    # url(r'^$', 'SysUp_JHFolheados.views.home', name='home'),

    (r'^$', 'home'),
    #(r'^$', 'add_usuario'),
    #(r'^$', 'ver_usuario'),
    #(r'^$', 'pesquisa_usuario'),
    #(r'^$', 'update_usuario'),
    #(r'^$', 'update_usuario'),
)
