from django.conf.urls import url
from drdown.appointments.views.view_appointment import (
    AppointmentListView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentMonthArchiveView,
    AppointmentUpdateStatusView,
    AppointmentFromRequestCreateView,
)
from drdown.appointments.views.view_request import (
    RequestListView,
    RequestCreateView,
    RequestUpdateView,
    RequestDeleteView,
    RequestUpdateStatusView,
)


app_name = 'appointments'
urlpatterns = [
    url(
        regex=r'^$',
        view=AppointmentListView.as_view(),
        name='list_appointments'
    ),
    url(
        regex=r'^request/new/$',
        view=RequestCreateView.as_view(),
        name='create_request'
    ),
    url(
        regex=r'^requests/$',
        view=RequestListView.as_view(),
        name='list_requests'
    ),
    url(
        regex=r'^request/update/(?P<request_pk>\d+)/$',
        view=RequestUpdateView.as_view(),
        name='update_request'
    ),
    url(
        regex=r'^request/delete/(?P<request_pk>\d+)/$',
        view=RequestDeleteView.as_view(),
        name='delete_request'
    ),
    url(
        regex=r'^new/$',
        view=AppointmentCreateView.as_view(),
        name='create_appointment'
    ),
    url(
        regex=r'^new/(?P<request_pk>\d+)/$',
        view=AppointmentFromRequestCreateView.as_view(),
        name='create_from_request'
    ),
    url(
        regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        view=AppointmentMonthArchiveView.as_view(month_format='%m'),
        name="archive_month"
    ),
    url(
        regex=r'^update/(?P<appointment_pk>\d+)/$',
        view=AppointmentUpdateView.as_view(),
        name='update_appointment'
    ),
    url(
        regex=r'^cancel/(?P<appointment_pk>\d+)/$',
        view=AppointmentUpdateStatusView.as_view(),
        name='update_status_appointment'
    ),
    url(
        regex=r'^request/cancel/(?P<request_pk>\d+)/$',
        view=RequestUpdateStatusView.as_view(),
        name='update_status_request'
    ),
]
