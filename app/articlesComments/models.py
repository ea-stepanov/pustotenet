# -*- encoding: utf-8 -*-
from django.db import models
from articles.models import Article

# Create your models here.
class ArticleComment(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    #subject = models.CharField(max_length=150, blank=True, verbose_name='Тема')
    message = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(verbose_name='Дата написания')
    show_status = models.BooleanField(verbose_name='Разрешить комментарий')
    article = models.ForeignKey(Article, related_name='comments', verbose_name='Статья')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий к статье'
        verbose_name_plural = 'Комментарии к статье'