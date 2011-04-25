# Create your views here.
from news.models import Notice
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from utils import ContextHackMixin
from django import forms

class NoticeForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'mce'}))
    class Meta:
        model = Notice

class NoticeList(ContextHackMixin, ListView):
    model = Notice

class NoticeAdd(ContextHackMixin, CreateView):
    model = Notice
    form_class = NoticeForm

class NoticeUpdate(ContextHackMixin, UpdateView):
    model = Notice
    form_class = NoticeForm
