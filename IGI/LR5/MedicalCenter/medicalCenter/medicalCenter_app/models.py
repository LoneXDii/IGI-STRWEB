from tkinter import CASCADE
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

#todo redo user model


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birth_date = models.DateField(validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365))], null=True)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='imgs/avatars', default='default_avatar.png')
    USERNAME_FIELD = 'name'


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=40)


class Service(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(validators=[MinValueValidator(0)])
    specialization_required = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)    


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birth_date = models.DateField(validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365))], null=True)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='imgs/avatars', default='default_avatar.png')
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)


class Appointment(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)


class Diagnosis(models.Model):
    name = models.CharField(max_length=40)
    setting_date = models.DateField()
    status = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)



class About(models.Model):
    text = models.CharField(max_length=1000)

class News(models.Model):
    header = models.CharField(max_length=300)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imgs/news_imgs', default='no_img.png')

class Term(models.Model):
    term = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

class Contacts(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    email = models.EmailField()

class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    requirements = models.CharField(max_length=200)
    salary = models.FloatField(validators=[MinValueValidator(0)])

class Review(models.Model):
    sender = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    mark = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    date = models.DateField()

class Coupons(models.Model):
    coupon = models.CharField(max_length=10)
    status = models.BooleanField()
    description = models.CharField(max_length=100)
    #services
    discount = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(10)])


