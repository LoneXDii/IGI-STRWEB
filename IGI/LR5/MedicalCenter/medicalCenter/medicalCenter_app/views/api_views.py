import os
import tempfile
from django.core import files
from django.http import HttpResponse
from django.shortcuts import render
import requests

from medicalCenter_app.models import News


class Joke():
    def __init__(self):
        self._setup = ''
        self._punchline = ''

    @property
    def setup(self):
        return self._setup
    
    @setup.setter
    def setup(self, value):
        self._setup = value

    @property
    def punchline(self):
        return self._punchline
    
    @punchline.setter
    def punchline(self, value):
        self._punchline = value

def jokes(request):
    responce = requests.get('https://official-joke-api.appspot.com/jokes/general/ten')
    responce = responce.json()
    jokes = list()
    for r_part in responce:
        joke = Joke()
        joke.setup = r_part['setup']
        joke.punchline = r_part['punchline']
        jokes.append(joke)
    return render(request, 'jokes.html', {'jokes': jokes})


def download_image_from_url(url):
    try:
        request = requests.get(url, stream=True)
    except requests.exceptions.RequestException as e:
        return None

    if request.status_code != requests.codes.ok:
        return None

    lf = tempfile.NamedTemporaryFile()

    for block in request.iter_content(1024 * 8):
        if not block:
            break
        lf.write(block)
    return files.File(lf)


def update_news():
    responce = requests.get('https://newsapi.org/v2/everything?language=ru&q=medicine&excludeDomains=mail.ru&apiKey=50aff5d34e9d484a828144e8ca7edf79')
    responce = responce.json()
    articles = responce['articles']
    for article in articles:
        try:
            temp = News.objects.get(title=article['title'])
            in_db = True
        except:
            in_db = False
        if not in_db:
            news_obj = News()
            news_obj.title = article['title']
            news_obj.description = article['description']
            news_obj.url = article['url']
            news_obj.image_url = article['urlToImage']
            news_obj.save_image_from_url()
            news_obj.save()
    return

def news(request):
    update_news()
    news_data = News.objects.all()
    data = {'news': news_data}
    return render(request, 'news.html', context=data)