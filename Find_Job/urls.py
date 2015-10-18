from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Find_Job.views.home', name='home'),
    # url(r'^Find_Job/', include('Find_Job.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^FindJob/', include('Site.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

