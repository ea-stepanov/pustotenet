# -*- coding: utf-8 -*-
from django.contrib import admin
from videoComments.models import Video

class VideoAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'authors', 'inlineCode', )
    list_display = ('name', )

admin.site.register(Video, VideoAdmin)
  