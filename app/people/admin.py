#-*- coding: utf-8 -*-
__author__ = 'eduard'

from django.contrib import admin
from models import Man

class ManAdmin(admin.ModelAdmin):
    fields = ('name', 'photo', 'contacts', 'information',)
    list_display = ('name',)

admin.site.register(Man, ManAdmin)
  