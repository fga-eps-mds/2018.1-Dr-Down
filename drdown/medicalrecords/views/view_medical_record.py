from django.shortcuts import render
from ..models.model_medical_record import MedicalRecord
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone


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
                'pk': self.kwargs.get('pk'),
            }
        )
        return success_create_url

    def form_valid(self, form):
        # Get category that post belongs to
        form.instance.author = self.request.user
        form.save()
        return super(MedicalRecordsCreateView, self).form_valid(form)
