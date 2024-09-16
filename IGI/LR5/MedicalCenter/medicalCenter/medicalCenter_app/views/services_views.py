from datetime import timedelta
import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from medicalCenter_app.forms import ServiceAppointmentForm, CartAddProductForm
from medicalCenter_app.models import Appointment, Client, Doctor, DoctorSpecialization, Service
from medicalCenter_app.cart import Cart


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
    

def get_times(time_min, time_max):
    time_obj = time_min
    times = list()
    step = timedelta(minutes=15)
    while time_obj < time_max:
        times.append(time_obj.strftime("%H:%M"))
        time_obj = (datetime.datetime.combine(datetime.date(1,1,1), time_obj) + step).time()
    return times


@login_required 
def service_appointment(request, service_id):
    if request.method == 'POST':
        form = ServiceAppointmentForm(request.POST)
        time = request.POST.get('time')
        time = datetime.datetime.strptime(time, "%H:%M").time()
        if form.is_valid():
            appointment = form.save()
            appointment.time = time
            temp = Appointment.objects.filter(doctor=appointment.doctor, date=appointment.date, time=time)
            if len(temp) == 0:
                client = request.POST.get('user_pk')
                if client is None   :
                    appointment.client = request.user.client
                else:
                    appointment.client = Client.objects.get(pk=int(client))
                appointment.service = Service.objects.get(pk=service_id)
                appointment.save()
                appointment.doctor.clients.add(appointment.client)
                return HttpResponseRedirect(reverse('services'))
            else:
                appointment.delete()
                service = Service.objects.get(pk=service_id)
                form.fields['doctor'].queryset = Doctor.objects.filter(specialization=service.specialization_required)
                time_min = Doctor.objects.first().shcedule.work_starts
                time_max = Doctor.objects.first().shcedule.work_ends
                times = get_times(time_min, time_max)
                timeok = False
                data = {'form': form, 'service': service, 'time': times, 'timeok': timeok}
                return render(request, 'services/service_appointment.html', data)
        else:
            service = Service.objects.get(pk=service_id)
            form.fields['doctor'].queryset = Doctor.objects.filter(specialization=service.specialization_required)
            time_min = Doctor.objects.first().shcedule.work_starts
            time_max = Doctor.objects.first().shcedule.work_ends
            times = get_times(time_min, time_max)
            timeok = True
            data = {'form': form, 'service': service, 'time': times, 'timeok': timeok}
            return render(request, 'services/service_appointment.html', data)
    else:
        service = Service.objects.get(pk=service_id)
        form = ServiceAppointmentForm()
        form.fields['doctor'].queryset = Doctor.objects.filter(specialization=service.specialization_required)
        time_min = Doctor.objects.first().shcedule.work_starts
        time_max = Doctor.objects.first().shcedule.work_ends
        times = get_times(time_min, time_max)
        timeok = True
        data = {'form': form, 'service': service, 'time': times, 'timeok': timeok}
        return render(request, 'services/service_appointment.html', data)


@login_required
def cart_appointment(request):
    if request.method == 'POST':
        form = ServiceAppointmentForm(request.POST)
        time = request.POST.get('time')
        time = datetime.datetime.strptime(time, "%H:%M").time()
        if form.is_valid():
            appointment = form.save()
            temp = Appointment.objects.filter(doctor=appointment.doctor, date=appointment.date, time=time)
            if len(temp) == 0:
                client = request.POST.get('user_pk')
                cart = Cart(request)
                service_ids = cart.cart.keys()
                lst_services = list()
                for service_id in service_ids:
                    lst_services.append(get_object_or_404(Service, id=service_id))
                
                appointment_lst = list()
                for service in lst_services:
                    app = Appointment()
                    app.doctor = appointment.doctor
                    app.date = appointment.date
                    app.service = service
                    app.time = time
                    app.count = cart.cart[str(service.pk)]['quantity']
                    appointment_lst.append(app)
                appointment.delete
                cart.clear()
                for app in appointment_lst:
                    if client is None   :
                        app.client = request.user.client
                    else:
                        app.client = Client.objects.get(pk=int(client))
                    app.save()
                    app.doctor.clients.add(app.client)

                return HttpResponseRedirect(reverse('services'))
            else:
                appointment.delete()
                cart = Cart(request)
                service_ids = cart.cart.keys()
                lst_services = list()
                for service_id in service_ids:
                    lst_services.append(get_object_or_404(Service, id=service_id))
                form = ServiceAppointmentForm()
                form.fields['doctor'].queryset = Doctor.objects.filter(specialization=lst_services[0].specialization_required)
                time_min = Doctor.objects.first().shcedule.work_starts
                time_max = Doctor.objects.first().shcedule.work_ends
                times = get_times(time_min, time_max)
                timeok = True
                data = {'services' : lst_services, 'time': times, 'form' : form, 'timeok': timeok}
                return render(request, 'cart/cart_appointment.html', data)
        else:
            cart = Cart(request)
            service_ids = cart.cart.keys()
            lst_services = list()
            for service_id in service_ids:
                lst_services.append(get_object_or_404(Service, id=service_id))
            form = ServiceAppointmentForm()
            form.fields['doctor'].queryset = Doctor.objects.filter(specialization=lst_services[0].specialization_required)
            time_min = Doctor.objects.first().shcedule.work_starts
            time_max = Doctor.objects.first().shcedule.work_ends
            times = get_times(time_min, time_max)
            timeok = True
            data = {'services' : lst_services, 'time': times, 'form' : form, 'timeok': timeok}
            return render(request, 'cart/cart_appointment.html', data)
    else:
        cart = Cart(request)
        service_ids = cart.cart.keys()
        lst_services = list()
        for service_id in service_ids:
            lst_services.append(get_object_or_404(Service, id=service_id))
        form = ServiceAppointmentForm()
        form.fields['doctor'].queryset = Doctor.objects.filter(specialization=lst_services[0].specialization_required)
        time_min = Doctor.objects.first().shcedule.work_starts
        time_max = Doctor.objects.first().shcedule.work_ends
        times = get_times(time_min, time_max)
        timeok = True
        data = {'services' : lst_services, 'time': times, 'form' : form, 'timeok': timeok}
        return render(request, 'cart/cart_appointment.html', data)
    

def service_info(request, service_id):
    service = Service.objects.get(pk=service_id)
    doctors = Doctor.objects.filter(specialization=service.specialization_required)
    form = CartAddProductForm()
    data = {'service' : service, 'doctors' : doctors, 'form' : form}
    return render(request, 'services/service_info.html', data)