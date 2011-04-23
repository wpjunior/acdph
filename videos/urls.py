from django.conf.urls.defaults import patterns, include, url
from videos.views import VideoList, VideoCreate

urlpatterns = patterns('albuns.views',
    url(r'^$', VideoList.as_view()),
                       #TODO: require login
    url(r'^add/$', VideoCreate.as_view()),
    url(r'action/$', 'album_action'), #TODO require login
)
