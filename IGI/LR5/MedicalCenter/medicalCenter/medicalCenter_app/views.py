from django.conf.locale import da
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from medicalCenter_app.forms import LoginForm, ProfileRegistrationForm, UserRegistrationForm
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

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    dj_login(request, user)
                    return HttpResponseRedirect(reverse('profile'))
                else:
                    return HttpResponse('Not ok')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            user.save()
            profile.user = user
            profile.save()
            dj_login(request, user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request):
    user = request.user
    try:
        profile = user.client
    except:
        profile = None

    if profile is None:
        try:    
            profile = user.doctor
        except:
            profile = None
    return render(request, 'account/profile.html', {'profile': profile})    

@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('login'))

def services(request):
    specalizations = DoctorSpecialization.objects.all()
    data = {'specializations': specalizations}
    return render(request, 'doctors_specializations.html', context=data)

def services_details(request, id):
    spec = DoctorSpecialization.objects.get(pk=id)
    data_obj = spec.service_set.all()
    data= {'services': data_obj}
    return render(request, 'doctor_services.html', context=data)