from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from medicalCenter_app.forms import LoginForm, ProfileRegistrationForm, ServiceAppointmentForm, UserRegistrationForm
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from medicalCenter_app.models import Appointment


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
    is_doctor = False
    try:
        profile = user.client
    except:
        profile = None

    if profile is None:
        try:    
            profile = user.doctor
            is_doctor = True
        except:
            profile = None
    data = {'profile': profile, 'is_doctor': is_doctor}
    return render(request, 'account/profile.html', data)    


@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def user_appointments(request):
    user = request.user
    try:
        profile = user.doctor
        appointments = Appointment.objects.filter(doctor=profile)
        is_doctor = True
        data = {'appointments' : appointments, 'doctor': is_doctor}
        return render(request, 'account/appointments.html', data)
    except:
        profile = None

    try:
        profile = user.client
        appointments = Appointment.objects.filter(client=profile)
        is_doctor = False
        data = {'appointments' : appointments, 'doctor': is_doctor}
        return render(request, 'account/appointments.html', data)
    except:
        return Http404()