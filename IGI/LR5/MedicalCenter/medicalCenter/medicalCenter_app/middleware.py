import calendar
import datetime
from django.conf import settings
import requests
import zoneinfo
from django.utils import timezone


def get_ip_adress(request):
    if settings.DEBUG:
        response = requests.get('https://api.ipify.org/?format=json')
        my_ip = response.json()['ip']
        return my_ip
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_info_user_by_ip(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/geo')
    return response.json()


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        else:
            response = get_info_user_by_ip(get_ip_adress(request))
            if 'timezone' in response:
                tzname = response['timezone']
            else:
                tzname =settings.TIME_ZONE
            request.session["django_timezone"] = tzname
            timezone.activate(zoneinfo.ZoneInfo(tzname))

        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if hasattr(response,'context_data'):
            tzname = request.session.get("django_timezone")
            my_calendar = calendar.TextCalendar()
            today = datetime.datetime.now(zoneinfo.ZoneInfo(tzname))
            my_calendar = my_calendar.formatmonth(today.year, today.month)
            if response.context_data:
                response.context_data['calendar'] = my_calendar
            else:
                response.context_data = {'calendar': my_calendar}
        return response