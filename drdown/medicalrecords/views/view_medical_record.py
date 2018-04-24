from django.shortcuts import render
from ..models.model_medical_record import MedicalRecord
from django.views.generic import ListView
from django.views.generic import DetailView
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
    success_url = reverse_lazy('medicalrecords:list_medicalrecords')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(MedicalRecordsCreateView, self).form_valid(form)


class MedicalRecordsDeleteView(DeleteView):
    model = MedicalRecord
    success_url = reverse_lazy('medicalrecords:list_medicalrecords')


class MedicalRecordsUpdateView(UpdateView):
    template_name = 'medicalrecords/medicalrecord_form.html'
    fields = ['patient', 'message']
    model = MedicalRecord
    success_url = reverse_lazy('medicalrecords:list_medicalrecords')
