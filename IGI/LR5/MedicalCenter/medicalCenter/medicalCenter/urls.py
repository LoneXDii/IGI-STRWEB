"""
URL configuration for medicalCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
import django.contrib.auth.urls
from django.urls import include, path
from medicalCenter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('coupons/', views.coupons, name='coupons'),
    path('news/', views.news, name='news'),
    path('privacy/', views.privacy, name='privacy'),
    path('reviews/', views.reviews, name='reviews'),
    path('terms/', views.terms_and_defs, name='terms'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
