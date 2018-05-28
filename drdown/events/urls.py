from django.conf.urls import url
from drdown.events.views.view_event import EventsListView
from drdown.events.views.view_event import EventsCreateView
from drdown.events.views.view_event import EventsUpdateView

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
    url(
    	regex = r'^update/(?P<pk>\d+)/$',
    	view = EventsUpdateView.as_view(),
    	name = 'update_event'
     ),
]
