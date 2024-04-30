from django.shortcuts import render
from medicalCenter_app.models import  News, Review


def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def coupons(request):
    return render(request, 'coupons.html')

def index(request):
    return render(request, 'index.html')

def news(request):
    news_data = News.objects.all()
    data = {'news': news_data}
    return render(request, 'news.html', context=data)

def privacy(request):
    return render(request, 'privacy.html')

def reviews(request):
    review_data = Review.objects.all()
    data = {'reviews': review_data}
    return render(request, 'reviews.html', context=data)

def terms_and_defs(request):
    return render(request, 'termsAndDefs.html')

def vacancies(request):
    return render(request, 'vacancies.html')