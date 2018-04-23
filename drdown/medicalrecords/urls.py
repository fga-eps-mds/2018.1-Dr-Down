from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from drdown.medicalrecords.views import view_medical_record

app_name = 'medicalrecords'
urlpatterns = [
    url(
        regex=r'^$',
        view=view_medical_record.MedicalRecordsListView.as_view(),
        name='list_medicalrecords'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
