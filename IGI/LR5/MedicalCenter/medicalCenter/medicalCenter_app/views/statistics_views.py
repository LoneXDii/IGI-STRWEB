import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loaders import app_directories
from medicalCenter_app.models import Appointment, Client
import plotly.graph_objs as go


def statistics(request):
    if not request.user.is_superuser:
        raise Http404()

    appointments = Appointment.objects.all()
    total_sum = 0
    get_sum = 0
    not_get_sum = 0
    for a in appointments:
        if a.is_active:
            not_get_sum += a.service.price
        else:
            get_sum += a.service.price
        total_sum += a.service.price

    data = {'total': total_sum, 'recieved': get_sum, 'not_recieved': not_get_sum}
    return render(request, 'statistics/main.html', data)


def age_statistics(request):
    if not request.user.is_superuser:
        raise Http404()

    age_groups = [
        (19, 35),  # Молодежь
        (36, 60),  # Взрослые
        (61, 100)  # Пожилые
    ]

    clients = Client.objects.all()
    for client in clients:
        if client.age == 0:
            bd = client.birth_date
            d = datetime.date.today()
            client.age = int((d - bd).days / 365)
            client.save()

    clients_in_group = [
        Client.objects.filter(age__range=(lower_bound, upper_bound)).count()
        for lower_bound, upper_bound in age_groups
    ]

    labels = ['Молодежь(19-35)', 'Взрослые(36-60)', 'Пожилые(61-100)']
    values = clients_in_group

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title='Распределение клиентов по возрасту')

    chart = fig.to_html(full_html=False)
    return HttpResponse(chart)


def statistics_by_user(request):
    if not request.user.is_superuser:
        raise Http404()
    clients = Client.objects.all()
    appointments = Appointment.objects.all()
    sums_active = list()
    sums_recieved = list()
    sums_total = list()
    for client in clients:
        sum_active = 0
        sum_recieved = 0
        total_sum = 0
        for appointment in appointments:
            if appointment.client == client:
                if appointment.is_active:
                    sum_active += appointment.service.price
                else:
                    sum_recieved += appointment.service.price
                total_sum += appointment.service.price
        sums_active.append(sum_active)
        sums_recieved.append(sum_recieved)
        sums_total.append(total_sum)
    data_couple = zip(clients, sums_active, sums_recieved, sums_total)
    return render(request, 'statistics/by_user.html', {'data': data_couple})