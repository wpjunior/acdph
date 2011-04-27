from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import Notice
from albuns.models import Album

def home(request):
    notices = Notice.objects.all()[:5]
    albums = Album.objects.all()[:5]

    return render_to_response("home.html", locals(),
                              context_instance=RequestContext(request))
