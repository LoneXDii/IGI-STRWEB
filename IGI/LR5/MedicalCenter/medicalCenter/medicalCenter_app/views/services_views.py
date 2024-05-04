from datetime import timedelta
import datetime
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from medicalCenter_app.forms import ServiceAppointmentForm
from medicalCenter_app.models import Doctor, DoctorSpecialization, Service


def services(request):
    specalizations = DoctorSpecialization.objects.all()
    user = request.user
    data = {'specializations': specalizations, 'user': user}
    return render(request, 'services/doctors_specializations.html', context=data)


def services_details(request, id):
    if request.method == 'POST':
        service_id = request.POST.get('appointment')
        return redirect(service_appointment, service_id=service_id)
    else:
        spec = DoctorSpecialization.objects.get(pk=id)
        data_obj = spec.service_set.all()

        sort_param = request.GET.get('sort_by')
        if sort_param == 'name':
            data_obj = list(data_obj.order_by('name'))
        elif sort_param == 'price':
            data_obj = list(data_obj.order_by('price'))

        try:
            doctor = request.user.doctor
            is_doctor = True
        except:
            is_doctor = False
        data= {'services': data_obj, 'doctor': is_doctor}
        return render(request, 'services/doctor_services.html', context=data)
    

@login_required 
def service_appointment(request, service_id):
    if request.method == 'POST':
        form = ServiceAppointmentForm(request.POST)
        time = request.POST.get('time')
        time = datetime.datetime.strptime(time, "%H:%M").time()
        if form.is_valid():
            appointment = form.save()
            appointment.client = request.user.client
            appointment.service = Service.objects.get(pk=service_id)
            appointment.save()
            appointment.doctor.clients.add(appointment.client)
            return HttpResponseRedirect(reverse('services'))
        else:
            service = Service.objects.get(pk=service_id)
            form.fields['doctor'].queryset = Doctor.objects.filter(specialization=service.specialization_required)
            data = {'form': form, 'service': service}
            return render(request, 'services/service_appointment.html', data)
    else:
        service = Service.objects.get(pk=service_id)
        form = ServiceAppointmentForm()
        form.fields['doctor'].queryset = Doctor.objects.filter(specialization=service.specialization_required)
        time_min = Doctor.objects.first().shcedule.work_starts
        time_max = Doctor.objects.first().shcedule.work_ends
        time_obj = time_min
        times = list()
        step = timedelta(minutes=15)
        while time_obj < time_max:
            times.append(time_obj.strftime("%H:%M"))
            time_obj = (datetime.datetime.combine(datetime.date(1,1,1), time_obj) + step).time()
        data = {'form': form, 'service': service, 'time': times}
        return render(request, 'services/service_appointment.html', data)