from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Diagnosis)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(DoctorSpecialization)