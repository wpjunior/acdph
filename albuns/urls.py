from django.conf.urls.defaults import patterns, include, url
from albuns.views import AlbumList, AlbumCreate, AlbumView

urlpatterns = patterns('albuns.views',
    url(r'^$', AlbumList.as_view()),
                       #TODO: require login
    url(r'^add/$', AlbumCreate.as_view()),
    url(r'^(?P<pk>\d+)/$', AlbumView.as_view()),
    url(r'^(?P<pk>\d+)/action/$', 'image_action'), #TODO require login
    url(r'action/$', 'album_action'), #TODO require login
)
