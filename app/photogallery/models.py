# -*- coding: utf-8 -*-
from django.db import models
from translit import get_translit
from PIL import Image

# Create your models here.
def _add_thumb(s):
    parts = s.split('.')
    parts.insert(-1, '.thumb')
    return '.'.join(parts)

class PhotoAlbum(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название альбома')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    cover = models.ImageField(upload_to='images/covers', verbose_name='Обложка')
    last_update_at = models.DateTimeField(verbose_name='Дата последнего обновления')
    link = models.SlugField(max_length=100) #absolute album url

    class Meta:
        ordering = ['name']
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбомы'

    def get_absolute_url(self):
        return '/' + self.link

    def __unicode__(self):
        return self.name

    def save(self):
        self.link = 'photogallery/%s' % get_translit(self.name)
        super(PhotoAlbum,self).save()
        #changing cover size
        temp = self.cover.path
        img = Image.open(self.cover.path)
        img.thumbnail((200,200), Image.ANTIALIAS)
        img.save(self.cover.path, 'JPEG', quality=100)


class Photo(models.Model):
    description = models.CharField(max_length=300, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    album = models.ForeignKey(PhotoAlbum, related_name='photos')
    photo = models.ImageField(upload_to='images/photos', verbose_name='Фотография')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def get_absolute_url(self):
        return self.photo.url

    def get_thumb_url(self):
        return _add_thumb(self.photo.url)

    def get_thumb_width(self):
        img = Image.open(_add_thumb(self.photo.path))
        return img.size[0]

    def get_thumb_height(self):
        img = Image.open(_add_thumb(self.photo.path))
        return img.size[1]

    def save(self):
        super(Photo,self).save()
        #add thumbnail
        img = Image.open(self.photo.path);
        img.thumbnail((200,200), Image.ANTIALIAS)
        img.save(_add_thumb(self.photo.path), 'JPEG', quality=80)
        #need to change last updated date of the photo album
        if (self.album.last_update_at == None or self.album.last_update_at < self.created_at):
            self.album.last_update_at = self.created_at