from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from acdph.views import LatestEntriesFeed
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^auth/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^auth/login/$', 'django.contrib.auth.views.login'),
    url(r'^media/(.*)','django.views.static.serve',{'document_root':MEDIA_ROOT}),
    url(r'^$', 'acdph.views.home', name='home'),
    url(r'^faleconosco/$', 'acdph.views.faleconosco', name='faleconosco'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^news/', include('acdph.news.urls')),
    url(r'^albuns/', include('acdph.albuns.urls')),
    url(r'^videos/', include('acdph.videos.urls')),
    url(r'^rss/', LatestEntriesFeed()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
