# -*- coding: utf-8 -*-
__author__ = 'eduard'

from django.contrib import admin
from models import ArticleComment

class ArticleCommentAdmin(admin.ModelAdmin):
    fields = ('name', 'message', 'created', 'show_status',)
    list_display = ('name', 'created', 'article',)

admin.site.register(ArticleComment, ArticleCommentAdmin)
  