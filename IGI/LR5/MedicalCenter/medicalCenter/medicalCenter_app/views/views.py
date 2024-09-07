from calendar import LocaleHTMLCalendar
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import dateformat, timezone
from medicalCenter_app.forms import ReviewForm
from medicalCenter_app.models import  About, Client, Coupons, Diagnosis, Doctor, News, Review, Term, Vacancy


def about(request):
    about = About.objects.get(pk=1)
    advantages = about.advantages.all()
    data = {'about': about, 'advantages': advantages}
    return render(request, 'about.html', context=data)

def contacts(request):
    doctors = Doctor.objects.all()
    data = {'doctors': doctors}
    return render(request, 'contacts.html', context=data)

def coupons(request):
    actual = Coupons.objects.filter(status=True)
    archive = Coupons.objects.filter(status=False)
    data = {'actual': actual, 'archive': archive}
    return render(request, 'coupons.html', context=data)

def index(request):
    time = timezone.datetime.now()
    date = dateformat.format(time, 'd/m/Y')
    
    last_news = News.objects.latest('id')
    data = {'date': date, "ln": last_news}
    return TemplateResponse(request, 'index.html', context=data)

def privacy(request):
    return render(request, 'privacy.html')

def reviews(request):
    review_data = Review.objects.all()
    authorized = request.user.is_authenticated
    data = {'reviews': review_data, 'authorized': authorized}
    return render(request, 'reviews.html', context=data)

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.sender = request.user.client
            review.date = datetime.today()
            review.save()
            return HttpResponseRedirect(reverse('reviews'))
        else:
            return render(request, 'addReview.html', {'form': form}) 
    else:
      form = ReviewForm()
      return render(request, 'addReview.html', {'form': form}) 

def terms_and_defs(request):
    terms = Term.objects.all()
    data = {'terms': terms}
    return render(request, 'termsAndDefs.html', context=data)

def vacancies(request):
    vacancies = Vacancy.objects.all()
    data = {'vacancies': vacancies}
    return render(request, 'vacancies.html', context=data)

def doctor_info(request, id):
    doctor = Doctor.objects.get(pk=id)
    return render(request, 'doctor_info.html', {'doctor': doctor})


@login_required
def client_info(request, id):
    try:
        doctor = request.user.doctor
        client = Client.objects.get(pk=id)
        diagnosises = Diagnosis.objects.filter(client=client)
        return render(request, 'client_info.html', {'client': client, 'diagnosises': diagnosises})
    except:
        raise Http404()