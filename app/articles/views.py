# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from models import Article
from django.http import HttpResponse
import os, random
from PIL import Image, ImageFont, ImageDraw
from forms import CommentForm
from time import strftime
from articlesComments.models import ArticleComment
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

#get all articles
def get_articles_list(request):
    articles = Article.objects.all()
    return render_to_response('articles.html', RequestContext(request, {'articles': articles}))

def view_article(request,slug):
    article = Article.objects.get(link=slug)
    if article:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if request.POST.get('captcha','') != request.session['captcha_answer']:
                form.errors['captcha'] = ('Неверно введен код с картинки',)
            if form.is_valid():
                data = form.cleaned_data
                if data['name'] == '':
                    data['name'] = 'Гость'
                if data['captcha'] == request.session['captcha_answer']:
                    article_id = request.POST.get('article', '')
                    com = ArticleComment(
                        name=data['name'],
                        message = data['message'],
                        article = Article.objects.get(id=article_id),
                        show_status = False,
                        created = strftime("%Y-%m-%d %H:%M:%S"))
                    com.save()
                    return HttpResponseRedirect(request.get_full_path())
        else:
            form = CommentForm(
                initial = {'message': 'Комментарии подвергаются проверке до публикации'}
            )
        #Captcha building
        #Load a random font
        os.chdir(os.path.dirname(__file__))
        fontsdir = '../../media/fonts/'
        temp = os.listdir(fontsdir)
        fonts = os.listdir(fontsdir)
        font = ImageFont.truetype(fontsdir + random.choice(fonts), 50)

        #Get captcha numbers
        numb1 = random.randint(0,9)
        numb2 = random.randint(0,9)
        numb3 = random.randint(0,9)
        numb4 = random.randint(0,9)

        #Building captcha text
        cap_text = str(numb1) + str(numb2) + str(numb3) + str(numb4)
        request.session['captcha_answer'] = cap_text

        #Creating captcha image
        image = Image.new("RGBA", (100,100), (255,255,255,0))
        draw = ImageDraw.Draw(image)
        text_size = draw.textsize(cap_text,font)
        image = image.resize((text_size[0] + 20, text_size[1] + 10))
        draw = ImageDraw.Draw(image)

        #Drawing text
        draw.text((10,0), cap_text, font=font, fill='#000000')
        image.save('../../media/images/captcha.png', 'PNG', quality=100)
        #Image is done

        comments = article.comments.all().filter(show_status=True)

        return render_to_response('article.html', RequestContext(request, {'article': article, 'comments': comments, 'form': form}))
    else:
        return HttpResponse('Empty') #TODO it's good to return JSON object
