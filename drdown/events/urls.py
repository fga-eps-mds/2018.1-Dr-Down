from django.conf.urls import url
from drdown.events.views.view_event import EventsListView

app_name ='events'

urlpatterns = [
    url(
        regex=r'^$',
        view=EventsListView.as_view(),
        name='list_events'
    ),
]
