from drdown.users.models.model_health_team import HealthTeam
from ..models.model_medicines import Medicine
from ..models.model_medical_record import MedicalRecord
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from ..forms.medicines_forms import MedicineForm
from ..views.views_base import BaseViewForm, BaseViewUrl


class MedicinesCreateView(BaseViewForm, BaseViewUrl, CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicalrecords/medicalrecord_medicine_form.html'


class MedicinesUpdateView(BaseViewUrl, UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicalrecords/medicalrecord_medicine_form.html'
