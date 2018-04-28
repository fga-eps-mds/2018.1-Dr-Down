from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from drdown.medicalrecords.forms.medicalrecords_forms import MedicalRecordForm
from drdown.medicalrecords.views import view_medical_record

app_name = 'medicalrecords'
urlpatterns = [
    url(
        regex=r'list/(?P<username>[\w.@+-]+)$',
        view=view_medical_record.MedicalRecordsList.as_view(),
        name='list_medicalrecords'
    ),
    url(
        regex=r'^$',
        view=view_medical_record.PatientSearchList.as_view(
            template_name='medicalrecords/medicalrecord_patient_list.html'),
        name='list_users_medicalrecords'
    ),

    url(
        regex=r'search/$',
        view=view_medical_record.MedicalRecordsSearchList.as_view(
            template_name='medicalrecords/medicalrecord_search_list.html'),
        name='list_search_medicalrecords'
    ),


    url(
        regex=r'^(?P<username>[\w.@+-]+)/new',
        view=view_medical_record.MedicalRecordsCreateView.as_view(
            form_class=MedicalRecordForm),
        name='create_medicalrecords'
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
]
