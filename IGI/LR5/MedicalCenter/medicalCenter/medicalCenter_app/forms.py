import django
from django.contrib.auth import forms
from django.contrib.auth.models import User
import django.forms
from medicalCenter_app.models import Appointment, Client, Diagnosis, Review


class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
    

class ProfileRegistrationForm(django.forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'second_name', 'email', 'birth_date', 'adress', 'phone_number', 'image')
        widgets = {'birth_date': django.forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                   'image': django.forms.FileInput(attrs={'class':'form-control', 'required': False,})}


class LoginForm(django.forms.Form):
    username = django.forms.CharField()
    password = django.forms.CharField(widget=django.forms.PasswordInput)


class ServiceAppointmentForm(django.forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'date')
        widgets = {'date': django.forms.DateInput(attrs={'class':'form-control', 'type':'date'}),}


class ReviewForm(django.forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'mark')


class DiagnosisForm(django.forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ('name',)


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(django.forms.Form):
    quantity = django.forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = django.forms.BooleanField(required=False, initial=False, widget=django.forms.HiddenInput)