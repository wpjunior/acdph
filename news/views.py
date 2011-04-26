# Create your views here.
from news.models import Notice
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils import ContextHackMixin
from django import forms

class NoticeForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'mce'}))
    class Meta:
        model = Notice
        exclude = ('user',)

class NoticeList(ContextHackMixin, ListView):
    model = Notice
    paginate_by = 5

class NoticeAdd(ContextHackMixin, CreateView):
    model = Notice
    form_class = NoticeForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        return super(NoticeAdd, self).form_valid(obj)

class NoticeUpdate(ContextHackMixin, UpdateView):
    model = Notice
    form_class = NoticeForm

class NoticeDelete(ContextHackMixin, DeleteView):
    model = Notice
    success_url = "/news/"
