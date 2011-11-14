# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Man

def get_people_list(request):
    people = Man.objects.all()
    return render_to_response('people.html', RequestContext(request, {'people': people}))

def get_man(request, slug):
    man = Man.objects.get(link=slug)
    return render_to_response('man.html', RequestContext(request, {'man': man}))

def get_man_materials(request, id):
    man = Man.objects.get(id=id)
    articles = man.articles.all()
    videos = man.videos.all()
    return render_to_response('man_materials.html', RequestContext(request, {'man': man, 'articles': articles, 'videos': videos}))