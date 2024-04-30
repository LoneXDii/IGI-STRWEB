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
from django.urls import path, re_path
from medicalCenter_app.views import views
from medicalCenter_app.views import account_views
from medicalCenter_app.views import services_views


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
    path('services/appointment/<int:service_id>/', services_views.service_appointment, name='appointment'),
    path('services/<int:id>/', services_views.services_details, name='service_details'),
    path('services/', services_views.services, name='services'),
    path('accounts/register/', account_views.register, name='register'),
    path('accounts/profile/', account_views.profile, name='profile'),
    path('accounts/login/', account_views.login, name='login'),
    path('accounts/logout/', account_views.logout, name='logout'),
    path('accounts/appointments/', account_views.user_appointments, name='user_appointments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
