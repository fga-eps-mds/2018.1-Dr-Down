from django.conf.urls import url
from .views.view_notifcations import PatientNotificationsView
from .views.view_notifcations import ResponsibleNotificationsView
from .views.view_notifcations import EmployeeNotificationsView
from .views.view_notifcations import HealthTeamNotificationsView

app_name = 'notifications'

urlpatterns = [
    url(
        regex=r'^patient/$',
        view=PatientNotificationsView.as_view(),
        name='patient_notifications'
    ),
    url(
        regex=r'^responsible/$',
        view=ResponsibleNotificationsView.as_view(),
        name='responsible_notifications'
    ),
    url(
        regex=r'^healthteam/$',
        view=HealthTeamNotificationsView.as_view(),
        name='health_team_notifications'
    ),
    url(
        regex=r'^employee/$',
        view=EmployeeNotificationsView.as_view(),
        name='employee_notifications'
    ),

]

