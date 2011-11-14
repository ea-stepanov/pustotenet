# -*- coding: utf-8 -*-
__author__ = 'eduard'

from django import forms

class CommentWidget(forms.Textarea):
    class Media:
        css = {
            'all': ('../media/css/commentform.css',)
            }
        js = ('../media/js/comment.js',)
    

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Ваше имя',
                           widget=forms.TextInput(attrs={'max_length': 100, 'class': 'fields'}))
    message = forms.CharField(label='Сообщение',
                widget=CommentWidget(attrs={
                    'class': 'fields', 'onfocus': 'empty_field("Комментарии подвергаются проверке до публикации")'
                }),
                error_messages = {'required': "Введите текст сообщения"})
    captcha = forms.CharField(label='Код')