from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    date = models.DateField(validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365))])
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=40)


class Service(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(validators=[MinValueValidator(0)])
    specialization_required = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)    


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    date = models.DateField(validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365))])
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
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
    clients = models.ManyToManyField(Client)
