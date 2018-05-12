from django.contrib import admin
from .models.model_appointment import Appointment
from .models.model_request import AppointmentRequest

# Register your models here.
admin.site.register(Appointment)
admin.site.register(AppointmentRequest)
