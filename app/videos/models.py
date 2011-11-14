# -*- coding: utf-8 -*-
from django.db import models
from people.models import Man
from translit import get_translit

class Video(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    inlineCode = models.TextField(verbose_name='Youtube код для вставки')
    description = models.TextField(verbose_name='Описание')
    authors = models.ManyToManyField(Man, related_name='videos', verbose_name='Авторы')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    link = models.SlugField(max_length=200)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/' + self.link

    def save(self):
        self.link = 'videos/%s' % get_translit(self.name)
        super(Video,self).save()