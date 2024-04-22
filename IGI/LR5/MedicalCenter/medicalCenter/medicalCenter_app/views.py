from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def coupons(request):
    return render(request, 'coupons.html')

def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def privacy(request):
    return render(request, 'privacy.html')

def reviews(request):
    return render(request, 'reviews.html')

def terms_and_defs(request):
    return render(request, 'termsAndDefs.html')

def vacancies(request):
    return render(request, 'vacancies.html')
