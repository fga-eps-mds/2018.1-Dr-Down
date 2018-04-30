from django.conf.urls import url
from drdown.appointments.views.view_appointment import AppointmentListView

app_name = 'appointments'
urlpatterns = [
    url(
        regex=r'^$',
        view=AppointmentListView.as_view(),
        name='list_appointments'
    ),
]
