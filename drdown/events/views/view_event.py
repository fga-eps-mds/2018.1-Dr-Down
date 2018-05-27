from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models.model_events import Events

class EventList(ListView):
    model = Events
    slug_field = 'name'
    slug_url_kwarg = 'name'
