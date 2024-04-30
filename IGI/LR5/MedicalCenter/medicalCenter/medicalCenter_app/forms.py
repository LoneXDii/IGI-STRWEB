import datetime
import django
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.forms import widgets
import django.forms
from medicalCenter_app.models import Appointment, Client


class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
    

class ProfileRegistrationForm(django.forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'second_name', 'birth_date', 'adress', 'phone_number', )
        widgets = {'birth_date': django.forms.DateInput(attrs={'class':'form-control', 'type':'date'}),}

class LoginForm(django.forms.Form):
    username = django.forms.CharField()
    password = django.forms.CharField(widget=django.forms.PasswordInput)


class ServiceAppointmentForm(django.forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('description', 'date', 'time', 'doctor')
        widgets = {'date': django.forms.DateInput(attrs={'class':'form-control', 'type':'date'}),}