from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from medicalCenter_app.forms import ServiceAppointmentForm
from medicalCenter_app.models import DoctorSpecialization, Service


def services(request):
    specalizations = DoctorSpecialization.objects.all()
    user = request.user
    data = {'specializations': specalizations, 'user': user}
    return render(request, 'services/doctors_specializations.html', context=data)


def services_details(request, id):
    if request.method == 'POST':
        service_id = request.POST.get('appointment')
        return HttpResponseRedirect(reverse(f'services/appointment/{service_id}'))
    else:
        spec = DoctorSpecialization.objects.get(pk=id)
        data_obj = spec.service_set.all()
        data= {'services': data_obj}
        return render(request, 'services/doctor_services.html', context=data)
    

@login_required 
def service_appointment(request, service_id):
    if request.method == 'POST':
        form = ServiceAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            a = request.user.client
            appointment.client = request.user.client
            appointment.service = Service.objects.get(pk=service_id)
            appointment.save()
            return HttpResponse("ZAEBIS")
        else:
            service = Service.objects.get(pk=service_id)
            data = {'form': form, 'service': service}
            return render(request, 'services/service_appointment.html', data)
    else:
        form = ServiceAppointmentForm()
        service = Service.objects.get(pk=service_id)
        data = {'form': form, 'service': service}
        return render(request, 'services/service_appointment.html', data)