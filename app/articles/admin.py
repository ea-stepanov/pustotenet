# -*- coding: utf-8 -*-
__author__ = 'eduard'

from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'preview', 'authors',)
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
  