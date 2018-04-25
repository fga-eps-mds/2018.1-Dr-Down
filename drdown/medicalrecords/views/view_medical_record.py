from django.shortcuts import render
from ..models.model_medical_record import MedicalRecord
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from ..forms.medicalrecords_forms import MedicalRecordSearchForm


class MedicalRecordsFilter(BaseFilter):
    search_fields = {
        'search_text': ['message'],
    }


class MedicalRecordsSearchList(SearchListView):
    model = MedicalRecord
    paginate_by = 30
    template_name = "medicalrecords/medicalrecord_list.html"
    form_class = MedicalRecordSearchForm
    filter_class = MedicalRecordsFilter


class MedicalRecordsListView(ListView):
    model = MedicalRecord


class MedicalRecordsCreateView(CreateView):
    model = MedicalRecord
    template_name = 'medicalrecords/medicalrecord_form.html'
    fields = ['patient', 'message']

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_create_url

    def form_valid(self, form):
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
    template_name = 'medicalrecords/medicalrecord_form.html'
    fields = ['patient', 'message']
    model = MedicalRecord

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_create_url
