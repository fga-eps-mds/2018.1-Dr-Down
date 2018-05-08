from drdown.users.models.model_health_team import HealthTeam
from ..models.model_static_data import StaticData
from ..models.model_medical_record import MedicalRecord
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from ..forms.static_data_forms import StaticDataForm
from ..views.views_base import BaseViewForm, BaseViewUrl


class StaticDataCreateView(BaseViewUrl, BaseViewForm, CreateView):
    model = StaticData
    form_class = StaticDataForm
    template_name = 'medicalrecords/medicalrecord_static_data_form.html'


class StaticDataUpdateView(BaseViewUrl, UpdateView):
    model = StaticData
    form_class = StaticDataForm
    template_name = 'medicalrecords/medicalrecord_static_data_form.html'
    slug_url_kwarg = 'username'
    slug_field = 'patient__user__username'
