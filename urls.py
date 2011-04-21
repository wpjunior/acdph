from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^media/(.*)','django.views.static.serve',{'document_root':MEDIA_ROOT}),
    url(r'^$', 'terranossa.views.home', name='home'),
    url(r'^albuns/', include('terranossa.albuns.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
