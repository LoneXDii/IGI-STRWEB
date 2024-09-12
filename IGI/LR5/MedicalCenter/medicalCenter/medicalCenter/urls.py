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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from medicalCenter_app.views import views
from medicalCenter_app.views import account_views, services_views, statistics_views, api_views, cart_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^contacts/$', views.contacts, name='contacts'),
    re_path(r'^coupons/$', views.coupons, name='coupons'),
    re_path(r'^news/$', api_views.news, name='news'),
    re_path(r'^privacy/$', views.privacy, name='privacy'),
    re_path(r'^reviews/$', views.reviews, name='reviews'),
    re_path(r'^reviews/add/$', views.add_review, name='add_review'),
    re_path(r'^terms/$', views.terms_and_defs, name='terms'),
    re_path(r'^vacancies/$', views.vacancies, name='vacancies'),
    re_path(r'^services/appointment/(?P<service_id>\d+)/$', services_views.service_appointment, name='appointment'),
    re_path(r'^services/info/(?P<service_id>\d+)/$', services_views.service_info, name='service_info'),
    re_path(r'^services/(?P<id>\d+)/$', services_views.services_details, name='service_details'),
    re_path(r'^services/$', services_views.services, name='services'),
    re_path(r'^accounts/register/$', account_views.register, name='register'),
    re_path(r'^accounts/profile/$', account_views.profile, name='profile'),
    re_path(r'^accounts/login/$', account_views.login, name='login'),
    re_path(r'^accounts/logout/$', account_views.logout, name='logout'),
    re_path(r'^accounts/changePassword/$', account_views.change_password, name='change_password'),
    re_path(r'^accounts/editProfile/$', account_views.edit_profile, name='edit_profile'),
    re_path(r'^accounts/appointments/$', account_views.user_appointments, name='user_appointments'),
    re_path(r'^accounts/diagnosis/(?P<client_id>\d+)/$', account_views.set_diagnosis, name='diagnosis_set'),
    re_path(r'^doctorInfo/(?P<id>\d+)/$', views.doctor_info, name='doctor_info'),
    re_path(r'^clientInfo/(?P<id>\d+)/$', views.client_info, name='client_info'),
    re_path(r'^clientInfo/diagnosises/(?P<client_id>\d+)/$', account_views.diagnosises, name='client_diagnosises'),
    re_path(r'^statistics/$', statistics_views.statistics, name='statistics'),
    re_path(r'^statistics/ageStats/$', statistics_views.age_statistics, name='age_statistics'),
    re_path(r'^statistics/byUser/$', statistics_views.statistics_by_user, name='by_user_stats'),
    re_path(r'^jokes/$', api_views.jokes, name='jokes'),
    re_path(r'^test/$', views.test, name='test'),
    re_path(r'^cart/add/(?P<service_id>\d+)/$', cart_views.cart_add, name='cart_add'),
    re_path(r'^cart/remove/(?P<service_id>\d+)/$', cart_views.cart_remove, name='cart_remove'),
    re_path(r'^cart/$', cart_views.cart_detail, name='cart_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
