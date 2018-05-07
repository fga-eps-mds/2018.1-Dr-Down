from django.contrib import admin
from .models.model_medical_record import MedicalRecord
from .models.model_static_data import StaticData

admin.site.register(MedicalRecord)
admin.site.register(StaticData)
