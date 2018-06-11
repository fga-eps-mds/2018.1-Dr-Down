from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from drdown.events.models.model_events import Events
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


class BaseViewPermissions(UserPassesTestMixin):

    def test_func(self):
        return hasattr(self.request.user, 'employee')


class EventsListView(ListView):
    model = Events
    slug_field = 'name'
    slug_url_kwarg = 'name'
    template_name = 'events/events_list.html'


class EventsCreateView(BaseViewPermissions, CreateView):
    model = Events
    template_name = 'events/events_form.html'
    fields = [
        'free',
        'location',
        'name',
        'date',
        'time',
        'description',
        'organize_by',
        'value',
    ]

    success_url = reverse_lazy(
        viewname='events:list_events',
    )


class EventsUpdateView(BaseViewPermissions, UpdateView):
    model = Events
    template_name = 'events/events_form.html'
    fields = [
        'free',
        'location',
        'name',
        'date',
        'time',
        'description',
        'organize_by',
        'value',
    ]

    def get_object(self):
        event = Events.objects.get(
            pk=self.kwargs.get('pk')
        )
        return event

    success_url = reverse_lazy(
        viewname='events:list_events',
    )


class EventsDeleteView(BaseViewPermissions, DeleteView):
    model = Events
    success_url = reverse_lazy(
        viewname='events:list_events',
    )
