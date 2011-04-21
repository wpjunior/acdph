# Create your views here
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from albuns.models import Album, Photo
from hashlib import md5
from utils import JSONResponse
from os.path import splitext

class ContextHackMixin(object):
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        context['request'] = self.request
        if hasattr(self, "get_extra_context"):
            context.update(self.get_extra_context())
            
        return self.response_class(
            request = self.request,
            template = self.get_template_names(),
            context = RequestContext(self.request, context),
            **response_kwargs
        )

class AlbumList(ContextHackMixin, ListView):
    model = Album

class AlbumCreate(ContextHackMixin, CreateView):
    model = Album

class AlbumView(ContextHackMixin, DetailView):
    model = Album

def upload_image(request, pk):
    album = get_object_or_404(Album, pk=pk)

    try:
        file = request.FILES['file']
        contents = file.read()
        hash = md5(contents).hexdigest()
        b, ext = splitext(file.name)
        filename = "%s%s" %(hash, ext)

        p = Photo(content_object=album)

        p.image.save(filename, file)

        p.save()

    except Exception, e:
        return JSONResponse({'error': str(e)})
        
    return JSONResponse({'url': p.image.url, 'error': None})
