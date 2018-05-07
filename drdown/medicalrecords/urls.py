from django.conf.urls import url
from drdown.medicalrecords.forms.medicalrecords_forms import MedicalRecordForm
from drdown.medicalrecords.forms.static_data_forms import StaticDataForm
from drdown.medicalrecords.forms.medicines_forms import MedicineForm
from drdown.medicalrecords.forms.comlaint_forms import ComplaintForm
from drdown.medicalrecords.forms.specific_exams_forms import SpecificExamsForm
from drdown.medicalrecords.views import view_medical_record, view_static_data, \
    view_medicines, view_specific_exams, view_complaint

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
        regex=r'^(?P<username>[\w.@+-]+)/new-specific-exam/$',
        view=view_specific_exams.SpecificExamCreateView.as_view(
            form_class=SpecificExamsForm),
        name='create_specific_exam_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/new-complaint/$',
        view=view_complaint.ComplaintCreateView.as_view(
            form_class=ComplaintForm),
        name='create_complaint_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/(?P<pk>\d+)/delete/$',
        view=view_medical_record.MedicalRecordsDeleteView.as_view(),
        name='delete_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/(?P<pk>\d+)/update/$',
        view=view_medical_record.MedicalRecordsUpdateView.as_view(
            form_class=MedicalRecordForm),
        name='update_medicalrecords'
    ),

    url(
        regex=r'^(?P<username>[\w.@+-]+)/(?P<pk>\d+)/update-static-data/$',
        view=view_static_data.StaticDataUpdateView.as_view(
            form_class=StaticDataForm),
        name='update_static_data_medicalrecords'
    ),
]
