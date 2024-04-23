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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import django.contrib.auth.urls
from django.urls import include, path, re_path
from medicalCenter_app import views

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    path('', views.index),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^contacts', views.contacts, name='contacts'),
    re_path(r'^coupons', views.coupons, name='coupons'),
    re_path(r'^news', views.news, name='news'),
    re_path(r'^privacy', views.privacy, name='privacy'),
    re_path(r'^reviews', views.reviews, name='reviews'),
    re_path(r'^terms', views.terms_and_defs, name='terms'),
    re_path(r'^vacancies', views.vacancies, name='vacancies'),
    re_path(r'^register', views.register, name='register'),
    path('services/<int:id>/', views.services_details, name='service_details'),
    path('services/', views.services, name='services'),
    re_path(r'^accounts', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
