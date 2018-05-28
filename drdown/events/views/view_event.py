from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from drdown.events.models.model_events import Events
from django.urls import reverse

class EventsListView(ListView):
    model = Events
    slug_field = 'name'
    slug_url_kwarg = 'name'
    template_name = 'events_list.html'

class EventsCreateView(CreateView):
	model = Events
	template_name = 'events_form.html'
	fields = [
		'date',
		'time',
		'description',
		'organize_by',
		'value',
	]
	
	def get_success_url(self):
		print("Entrou no sucess url")
		success_create_url = reverse(
			viewname='events:list_events',
        )
		return success_create_url
