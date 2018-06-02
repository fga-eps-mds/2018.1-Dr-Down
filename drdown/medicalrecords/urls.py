from django.conf.urls import url
from drdown.medicalrecords.forms.exam_forms import ExamForm
from drdown.medicalrecords.forms.medicalrecords_forms import MedicalRecordForm
from drdown.medicalrecords.forms.static_data_forms import StaticDataForm
from drdown.medicalrecords.forms.medicines_forms import MedicineForm
from drdown.medicalrecords.forms.complaint_forms import ComplaintForm
from drdown.medicalrecords.forms.risk_forms import RiskForm
from drdown.medicalrecords.views import (
    view_medical_record, view_static_data,
    view_medicines, view_complaint, view_exams,
    view_pdf, view_risk, view_curves,
)

app_name = 'medicalrecords'
urlpatterns = [
    url(
        regex=r'list/(?P<username>[\w.@+-]+)/$',
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
    url(
        regex=r'^(?P<username>[\w.@+-]+)/new-medicine/$',
        view=view_medicines.MedicinesCreateView.as_view(
            form_class=MedicineForm),
        name='create_medicine'
    ),
    url(
        regex=r'(?P<username>[\w.@+-]+)/update-medicine/(?P<pk>\d+)/$',
        view=view_medicines.MedicinesUpdateView.as_view(
            form_class=MedicineForm),
        name='update_medicine'
    ),
    url(
        regex=r'(?P<username>[\w.@+-]+)/risk/edit/$',
        view=view_risk.RiskUpdateView.as_view(),
        name='update_risk'
    ),
    url(
        regex=r'(?P<username>[\w.@+-]+)/pdf/$',
        view=view_pdf.PDFView.as_view(),
        name='pdf'
    ),
    url(
        regex=r'(?P<username>[\w.@+-]+)/curves/create-height/$',
        view=view_curves.CurvesCreateView.as_view(),
        name='create_curve'
    ),
    url(
        regex=r'(?P<username>[\w.@+-]+)/curves/update-height/(?P<pk>\d+)/$',
        view=view_curves.CurvesUpdateView.as_view(),
        name='update_curve'
    ),
]
