from django.shortcuts import render
from ..models.model_medical_record import MedicalRecord
from drdown.users.models.model_patient import Patient
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.exceptions import ValidationError
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from ..forms.medicalrecords_forms import MedicalRecordSearchForm,\
    MedicalRecordCompleteSearchForm, PatientSearchForm, MedicalRecordForm


class MedicalRecordsFilter(BaseFilter):
    search_fields = {
        'search_text': ['message'],
        'search_date': ['day'],
        'author': ['author__id'],
        'patient': ['patient__id'],
        'message': ['message']
    }


class MedicalRecordsList(SearchListView):
    model = MedicalRecord
    template_name = "medicalrecords/medicalrecord_list.html"
    form_class = MedicalRecordSearchForm
    filter_class = MedicalRecordsFilter

    def related_patient(self):
        for patient in Patient.objects.all():
            if patient.user.username == self.kwargs.get('username'):
                return patient

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordsList, self).get_context_data(**kwargs)
        elect_count = 0
        for device in MedicalRecord.objects.all():
            if device.patient.user.username == self.kwargs.get('username'):
                elect_count += 1
        context['elect_count'] = elect_count
        return context


class MedicalRecordsSearchList(SearchListView):
    model = MedicalRecord
    template_name = "medicalrecords/medicalrecord_search_list.html"
    form_class = MedicalRecordCompleteSearchForm
    filter_class = MedicalRecordsFilter
    paginate_by = 10


class PatientSearchList(SearchListView):
    model = Patient
    template_name = "medicalrecords/medicalrecord_patient_list.html"
    form_class = PatientSearchForm
    filter_class = MedicalRecordsFilter
    paginate_by = 20


class MedicalRecordsCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'

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

        form.instance.author = self.request.user
        form.save()
        return super(MedicalRecordsCreateView, self).form_valid(form)


class MedicalRecordsDeleteView(DeleteView):
    model = MedicalRecord

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_create_url


class MedicalRecordsUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_create_url
