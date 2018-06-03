from django.conf.urls import url
from .views.view_notifcations import PatientNotificationsView


app_name = 'notifications'

urlpatterns = [
    url(
        regex=r'^$',
        view=PatientNotificationsView.as_view(),
        name='patient_notifications'
    ),

]

