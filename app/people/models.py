# -*- coding: utf-8 -*-
from django.db import models
from translit import get_translit

# Create your models here.
class Man(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя, Фамилия')
    photo = models.ImageField(blank=True, upload_to='images/people', verbose_name='Фотография') #TODO make unique names
    contacts = models.TextField(blank=True, verbose_name='Контакты') #TODO how contacts should be kept
    information = models.TextField(blank=True, verbose_name='Информация')
    link=models.SlugField(max_length=200)
    #TODO add video witnessing field
    
    class Meta:
        ordering=['name']
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def get_absolute_url(self):
        return '/' + self.link

    def __unicode__(self):
        return self.name

    def save(self):
        self.link = 'people/%s' % get_translit(self.name)
        super(Man,self).save()