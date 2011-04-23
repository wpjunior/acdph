# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from videos.models import Video
from utils import JSONResponse, ContextHackMixin
from django.http import Http404

class VideoList(ContextHackMixin, ListView):
    model = Video

class VideoCreate(ContextHackMixin, CreateView):
    model = Video
    success_url = "/videos/"
