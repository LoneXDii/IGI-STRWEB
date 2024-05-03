from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from medicalCenter_app.forms import ReviewForm
from medicalCenter_app.models import  Appointment, Client, Diagnosis, Doctor, News, Review


def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def coupons(request):
    return render(request, 'coupons.html')

def index(request):
    return render(request, 'index.html')

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
    return render(request, 'termsAndDefs.html')

def vacancies(request):
    return render(request, 'vacancies.html')

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