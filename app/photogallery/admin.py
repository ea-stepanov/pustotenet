# -*- coding: utf-8 -*-
__author__ = 'eduard'

from django.contrib import admin
from models import Photo, PhotoAlbum

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0

class PhotoAlbumAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'cover', 'last_update_at')
    list_display = ('name', 'created_at',)
    inlines = [
        PhotoInline,
    ]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at',)
    
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)