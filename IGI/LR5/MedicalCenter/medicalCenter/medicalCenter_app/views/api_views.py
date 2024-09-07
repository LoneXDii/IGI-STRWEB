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
            #news_obj.save_image_from_url()
            if (not news_obj.image_url is None):
                news_obj.save()
    return

def news(request):
    update_news()
    news_data = News.objects.all()
    data = {'news': reversed(news_data)}
    return render(request, 'news.html', context=data)