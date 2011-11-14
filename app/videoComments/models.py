# -*- encoding: utf-8 -*-
from django.db import models
from videos.models import Video

# Create your models here.
class VideoComment(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    #subject = models.CharField(max_length=150, blank=True, verbose_name='Тема')
    message = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(verbose_name='Дата написания', auto_now_add=True)
    show_status = models.BooleanField(verbose_name='Разрешить комментарий')
    video = models.ForeignKey(Video, related_name='comments', verbose_name='Видеоролик')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий к видео'
        verbose_name_plural = 'Комментарии к видео'