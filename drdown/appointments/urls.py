from django.conf.urls import url
from drdown.appointments.views.view_appointment import AppointmentListView
from drdown.appointments.views.view_appointment import AppointmentCreateView

app_name = 'appointments'
urlpatterns = [
    url(
        regex=r'^$',
        view=AppointmentListView.as_view(),
        name='list_appointments'
    ),
    url(
        regex=r'^new/$',
        view=AppointmentCreateView.as_view(),
        name='create_appointment'
    ),

]
