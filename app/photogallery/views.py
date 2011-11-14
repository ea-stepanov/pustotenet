# -*- coding: utf-8 -*-

from models import Photo, PhotoAlbum
from django.shortcuts import render_to_response
from django.template import RequestContext

def photogallery(request):
    albums = PhotoAlbum.objects.all();
    return render_to_response('photogallery.html', RequestContext(request, {'albums': albums}))

def view_gallery(request, slug):
    slug = slug.encode('utf-8')
    album = PhotoAlbum.objects.get(link=slug)
    photos = album.photos.all()

    #Photo grouping for table showing
    numb_in_row = 3; #number of photos in a table row
    gr_photos = [];
    for i in range(0, len(photos)/numb_in_row):
        gr_photos += [photos[numb_in_row*i:numb_in_row*i+numb_in_row]]
    gr_photos += [photos[len(photos)/numb_in_row*numb_in_row:]]
    return render_to_response('view_gallery.html', {'photos':gr_photos, 'album_name':album.name})