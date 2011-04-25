from django.conf.urls.defaults import patterns, include, url
from news.views import NoticeList, NoticeAdd, NoticeUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('news.views',
                       url(r'^$', NoticeList.as_view()),
                       url(r'^add/$', NoticeAdd.as_view()),
                       url(r'^edit/(?P<pk>\d+)/$', NoticeUpdate.as_view()),
)
