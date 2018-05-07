from drdown.users.models.model_health_team import HealthTeam
from ..models.model_medicines import Medicine
from ..models.model_medical_record import MedicalRecord
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from ..forms.medicines_forms import MedicineForm


class MedicinesCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicalrecords/medicalrecord_static_data_form.html'

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username')
            }
        )
        return success_create_url

    def form_valid(self, form):
        for patient in Patient.objects.all():
            if patient.user.username == self.kwargs.get('username'):
                form.instance.patient = patient
        user = User.objects.get(
            username=self.request.user
        )
        healthteam = HealthTeam.objects.get(
            user=user
        )
        form.instance.author = healthteam
        form.save()
        return super(MedicinesCreateView, self).form_valid(form)


class MedicinesUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicalrecords/medicalrecord_static_data_form.html'

    def get_success_url(self, **kwargs):
        success_update_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_update_url
