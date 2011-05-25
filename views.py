#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import Notice
from albuns.models import Album
from terranossa.captcha.fields import CaptchaField
from django.core.mail import send_mail, BadHeaderError
from django import forms
from terranossa.settings import FROM_EMAIL, TO_EMAIL
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.syndication.views import Feed

def home(request):
    notices = Notice.objects.filter(Q(category__id=2)|Q(category__id=3)|Q(category__id=4))[:5]
    opniao = Notice.objects.filter(category__id=1)[:5]
    albums = Album.objects.all()[:8]

    return render_to_response("home.html", locals(),
                              context_instance=RequestContext(request))

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=10)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField(label="Confirmação")

def faleconosco(request):

    if request.method == "POST":
        form = ContatoForm(request.POST)
    else:
        form = ContatoForm()

    if form.is_valid():
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        mensagem = request.POST['mensagem']

        t = loader.get_template('faleconosco_email.txt')
        c = Context(locals())
        text = t.render(c)

        print text

        try:
            send_mail("Mensagem FaleConosco", text, FROM_EMAIL, [TO_EMAIL])
        except Exception, e:
            print e
            erro = 'Erro ao Enviar Mensagem'
        else:
            return HttpResponseRedirect('/')

    return render_to_response("faleconosco.html", locals(),
                              context_instance=RequestContext(request))



class LatestEntriesFeed(Feed):
    title = "Noticias do Portal Terra Nossa"
    link = "/news/"
    description = "Noticias sobre opnião, municipio e estado de Corumbá de goiás"

    def items(self):
        return Notice.objects.all()[:5]

    def item_title(self, item):
        return item.name

    def item_author_name(self, obj):
        return obj.user.get_full_name()

    def item_author_email(self, obj):
        return obj.user.email

    def item_link(self, item):
        return "http://portalterranossa.com.br/news/%d/" % item.id
