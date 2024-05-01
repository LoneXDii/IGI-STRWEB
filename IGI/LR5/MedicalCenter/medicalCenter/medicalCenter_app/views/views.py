from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from medicalCenter_app.forms import ReviewForm
from medicalCenter_app.models import  Appointment, Client, Doctor, News, Review


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
    authorized = request.user.is_authenticated
    data = {'reviews': review_data, 'authorized': authorized}
    return render(request, 'reviews.html', context=data)

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.sender = request.user.client
            review.date = datetime.today()
            review.save()
            return HttpResponseRedirect(reverse('reviews'))
        else:
            return render(request, 'addReview.html', {'form': form}) 
    else:
      form = ReviewForm()
      return render(request, 'addReview.html', {'form': form}) 

def terms_and_defs(request):
    return render(request, 'termsAndDefs.html')

def vacancies(request):
    return render(request, 'vacancies.html')

def doctor_info(request, id):
    doctor = Doctor.objects.get(pk=id)
    return render(request, 'doctor_info.html', {'doctor': doctor})

def client_info(request, id):
    client = Client.objects.get(pk=id)
    return render(request, 'client_info.html', {'client': client})