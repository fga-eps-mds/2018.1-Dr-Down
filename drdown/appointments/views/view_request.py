from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from drdown.appointments.models import Request
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from ..forms.requests_form import RequestSearchForm


class RequestFilter(LoginRequiredMixin, BaseFilter):
    search_fields = {
        'search_speciality': ['speciality'],
        'search_doctor': ['doctor__id'],
        'search_patient': ['patient__id'],
        'search_status': ['status'],
    }


class RequestListView(LoginRequiredMixin, SearchListView):
    model = Request
    template_name = 'appointments/request_list.html'
    form_class = RequestSearchForm
    filter_class = RequestFilter
    paginate_by = 10
