from django.conf.locale import da
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from medicalCenter_app.models import Client, DoctorSpecialization, News, Review, Service

#todo redo user model

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

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        second_name = request.POST.get('second_name')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        user = User.objects.create_user(username, email, password)
        client = Client()
        client.user = user
        client.name = name
        client.second_name = second_name
        client.surname = surname
        client.birth_date = birth_date
        client.phone_number = phone_number
        client.adress = address

        user.save()
        client.save()
        return HttpResponseRedirect('')
    
def services(request):
    specalizations = DoctorSpecialization.objects.all()
    data = {'specializations': specalizations}
    return render(request, 'doctors_specializations.html', context=data)

def services_details(request, id):
    spec = DoctorSpecialization.objects.get(pk=id)
    data_obj = spec.service_set.all()
    data= {'services': data_obj}
    return render(request, 'doctor_services.html', context=data)