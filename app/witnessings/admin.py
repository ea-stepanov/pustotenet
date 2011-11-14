# -*- coding: utf-8 -*-
__author__ = 'eduard'

from django.contrib import admin
from models import Witnessing

class WitnessingAdmin(admin.ModelAdmin):
    fields = ('name', 'text', 'author', 'preview',)
    list_display = ('name',)

admin.site.register(Witnessing, WitnessingAdmin)