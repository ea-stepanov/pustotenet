# -*- coding: utf-8 -*-
__author__ = 'eduard'

from django.contrib import admin
from videoComments.models import VideoComment

class VideoCommentAdmin(admin.ModelAdmin):
    fields = ('name', 'message', 'show_status', 'video', )
    list_display = ('name', 'video', )

admin.site.register(VideoComment, VideoCommentAdmin)  