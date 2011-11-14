# -*- coding: utf-8 -*-
from django.db import models
from people.models import Man
from translit import get_translit

# Create your models here.
class Witnessing(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст статьи')
    author = models.OneToOneField(Man, related_name='witnessing', verbose_name='Автор')
    preview = models.TextField(blank=True, verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    link = models.SlugField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Свидетельство'
        verbose_name_plural = 'Свидетельства'

    def get_absolute_url(self):
        return self.link

    def __unicode__(self):
        return self.name

    def save(self):
        self.link = 'witnessings/%s' % get_translit(self.name)
        super(Witnessing,self).save()
