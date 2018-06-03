from django.conf.urls import url
from .views.view_notifcations import NotificationCenterView


app_name = 'notifications'

urlpatterns = [
    url(
        regex=r'^$',
        view=NotificationCenterView.as_view(),
        name='notifications'
    ),

]

