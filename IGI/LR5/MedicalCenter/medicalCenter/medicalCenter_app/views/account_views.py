import datetime
from django.contrib import messages
from django.contrib.auth import login as dj_login, update_session_auth_hash
from django.contrib.auth import logout as dj_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from medicalCenter_app.forms import DiagnosisForm, LoginForm, ProfileRegistrationForm, UserRegistrationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from medicalCenter_app.models import Appointment, Client, Diagnosis


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
    diagnosises = None
    try:
        profile = user.client
        diagnosises = Diagnosis.objects.filter(client=profile)
    except:
        profile = None

    if profile is None:
        try:    
            profile = user.doctor
            is_doctor = True
        except:
            profile = None
    data = {'profile': profile, 'is_doctor': is_doctor, 'diagnosises': diagnosises}
    return render(request, 'account/profile.html', data)    


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed.")
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = PasswordChangeForm(request.user)
        data = {'form': form}
        return render(request, "account/change_password.html", data) 


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile = request.user.client
        form = ProfileRegistrationForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return HttpResponseRedirect(reverse('profile'))
        else:
            return render(request, 'account/edit_profile.html', {'form': form})
    else:
        try:
            profile = request.user.client
        except:
            return HttpResponse('Для изменения профиля обратитесь к администратору')
        form = ProfileRegistrationForm(instance=profile)
        return render(request, 'account/edit_profile.html', {'form': form})


@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def set_diagnosis(request, client_id):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            diagnosis = form.save()
            diagnosis.client = Client.objects.get(pk=client_id)
            diagnosis.doctor = request.user.doctor
            diagnosis.setting_date = datetime.date.today()
            diagnosis.save()
            return redirect(user_appointments)
    else:
        try:
            doctor = request.user.doctor
        except:
            return Http404()
        form = DiagnosisForm()
        return render(request, 'account/set_diagnosis.html', {'form': form})


@login_required
def user_appointments(request):
    if request.method == 'POST':
        appointment_id_close = request.POST.get('close')
        appointment_id_del = request.POST.get('del_button')
        if appointment_id_close is None:
            Appointment.objects.get(pk=int(appointment_id_del)).delete()
            user = request.user
            profile = user.client
            appointments = Appointment.objects.filter(client=profile)
            is_doctor = False
            data = {'appointments' : appointments, 'doctor': is_doctor}
            return render(request, 'account/appointments.html', data)
        else:
            appointment = Appointment.objects.get(pk=int(appointment_id_close))
            appointment.is_active = False
            appointment.save()
            user = request.user
            profile = user.doctor
            appointments = Appointment.objects.filter(doctor=profile)
            is_doctor = True
            data = {'appointments' : appointments, 'doctor': is_doctor}
            return redirect(set_diagnosis, client_id=appointment.client.pk)
    else:
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
        

