from django.contrib import admin
from .models.model_medical_record import MedicalRecord
from .models.model_static_data import StaticData
from .models.model_medicines import Medicine

admin.site.register(MedicalRecord)
admin.site.register(StaticData)
admin.site.register(Medicine)
