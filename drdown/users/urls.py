from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~delete/',
        view=views.UserDeleteView.as_view(),
        name='delete'
    ),
    url(
        regex=r'^~patients/$',
        view=views.PatientListViewSelector.as_view(),
        name='patient_list'
    ),
    url(
        regex=r'^~responsible/patients/$',
        view=views.ResponsiblePatientListView.as_view(),
        name='responsible_patient_list'
    ),
    url(
        regex=r'^~healthteam/patients/$',
        view=views.HealthTeamPatientListView.as_view(),
        name='healthteam_patient_list'
    ),
    url(
        regex=r'^~patients/(?P<username>[\w.@+-]+)$',
        view=views.PatientDetailView.as_view(),
        name='patient_medical_sheet'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
