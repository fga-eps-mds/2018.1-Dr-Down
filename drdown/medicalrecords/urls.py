from django.conf.urls import url
from drdown.medicalrecords.forms.exam_forms import ExamForm
from drdown.medicalrecords.forms.medicalrecords_forms import MedicalRecordForm
from drdown.medicalrecords.forms.static_data_forms import StaticDataForm
from drdown.medicalrecords.forms.medicines_forms import MedicineForm
from drdown.medicalrecords.forms.complaint_forms import ComplaintForm
from drdown.medicalrecords.views import view_medical_record, view_static_data,\
    view_medicines, view_complaint, view_exams

app_name = 'medicalrecords'
urlpatterns = [
    url(
        regex=r'list/(?P<username>[\w.@+-]+)$',
        view=view_medical_record.MedicalRecordsList.as_view(),
        name='list_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/new/$',
        view=view_medical_record.MedicalRecordsCreateView.as_view(
            form_class=MedicalRecordForm),
        name='create_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/new-static-data/$',
        view=view_static_data.StaticDataCreateView.as_view(
            form_class=StaticDataForm),
        name='create_static_data_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/new-medicine/$',
        view=view_medicines.MedicinesCreateView.as_view(
            form_class=MedicineForm),
        name='create_medicine_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/new-complaint/$',
        view=view_complaint.ComplaintCreateView.as_view(
            form_class=ComplaintForm),
        name='create_complaint_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/new-exam/$',
        view=view_exams.ExamCreateView.as_view(
            form_class=ExamForm),
        name='create_exam_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/update-static-data/$',
        view=view_static_data.StaticDataUpdateView.as_view(
            form_class=StaticDataForm),
        name='update_static_data_medicalrecords'
    ),
]
