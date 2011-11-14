# -*- conding: utf-8 -*-
__author__ = 'eduard'

from django.shortcuts import render_to_response

def main(request):
    return render_to_response('main.html')

def photogallery(request):
    return render_to_response('photogallery.html')

def people(request):
    return render_to_response('people.html')

def articles(request):
    return render_to_response('articles.html')