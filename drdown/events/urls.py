from django.conf.urls import url
from drdown.events.views.view_event import EventsListView
from drdown.events.views.view_event import EventsCreateView

app_name ='events'

urlpatterns = [
    url(
        regex = r'^$',
        view = EventsListView.as_view(),
        name = 'list_events'
    ),
    url(
    	regex = r'^new/$',
    	view = EventsCreateView.as_view(),
    	name = 'create_event'
    	),
]
