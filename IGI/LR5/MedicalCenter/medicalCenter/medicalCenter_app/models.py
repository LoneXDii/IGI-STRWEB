import os
from tempfile import NamedTemporaryFile
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime
import requests


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, default='baseemail@mail.ru')
    birth_date = models.DateField(validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365),
                                                             message="Вам должно быть не менее 18 лет для регистрации")], null=True)
    age = models.IntegerField(default=0)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13,
                                    validators=[RegexValidator(
                                        regex=r'^\+375(44|29)\d{7}$',
                                        message='Некорректный номер телефона'
                                    )])
    image = models.ImageField(upload_to='imgs/avatars', default='default_avatar.png')

    def __str__(self):
        return f"{self.surname} {self.name} {self.second_name}"


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField(validators=[MinValueValidator(0)])
    specialization_required = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.specialization_required.name})"    


class Schedule(models.Model):
    work_starts = models.TimeField()
    work_ends= models.TimeField()

    def __str__(self):
        return f"{self.work_starts} - {self.work_ends}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, default='baseemail@mail.ru')
    birth_date = models.DateField(validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=18 * 365),
                                                             message="Вам должно быть не менее 18 лет для регистрации")], null=True)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13,
                                    validators=[RegexValidator(
                                        regex=r'^\+375(44|29)\d{7}$',
                                        message='Некорректный номер телефона'
                                    )])
    image = models.ImageField(upload_to='imgs/avatars', default='default_avatar.png')
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)
    shcedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING, null=True)
    clients = models.ManyToManyField(Client, blank=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.second_name}"


class Appointment(models.Model):
    date = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    time = models.TimeField(null=True) #input format 12:20
    count = models.IntegerField(default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)


class Diagnosis(models.Model):
    name = models.CharField(max_length=40)
    setting_date = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)


class Advantage(models.Model):
    header = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)


class About(models.Model):
    logo = models.ImageField(upload_to="imgs", default="MC_Logo.jpg")
    start = models.CharField(max_length=1000, default='')
    advantages = models.ManyToManyField(Advantage)
    end = models.CharField(max_length=1000, default='')


class News(models.Model):
    title = models.CharField(max_length=1000, default='')
    description = models.CharField(max_length=1000, default='')
    url = models.URLField(max_length=1000, default='')
    image = models.ImageField(upload_to='imgs/news_imgs', default='no_img.png')
    image_url = models.URLField(max_length=1000, null=True)

    def save_image_from_url(self):
        if self.image_url is None:
            return False
        r = requests.get(self.image_url)
        if r.status_code == 200:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(r.content)
            img_temp.flush()
            try:
                self.image.save(os.path.basename(self.image_url), File(img_temp), save=True)
            except:
                print("Failed downloading image from ", self.image_url)
                return False
            else:
                return True
        else:
            return False


class Term(models.Model):
    term = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.term


class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    requirements = models.CharField(max_length=200)
    salary = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
    

class Review(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1000)
    mark = models.IntegerField(validators=[MaxValueValidator(5, message='Значение должно быть от 1 до 5'), MinValueValidator(1, message='Значение должно быть от 1 до 5')])
    date = models.DateField(null=True)


class Coupons(models.Model):
    name = models.CharField(max_length=50, default='')
    coupon = models.CharField(max_length=10, default='')
    status = models.BooleanField()
    discount = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(10)])

    def __str__(self):
        return self.name

