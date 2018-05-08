from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from drdown.appointments.models import AppointmentRequest
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
    model = AppointmentRequest
    template_name = 'appointments/request_list.html'
    form_class = RequestSearchForm
    filter_class = RequestFilter
    paginate_by = 10

    @staticmethod
    def prepare_queryset(request):
        user = request.user
        if hasattr(user, 'patient'):
            queryset = AppointmentRequest.objects.filter(
                patient=user.patient
            ).order_by('id')
        elif hasattr(user, 'responsible'):
            queryset = AppointmentRequest.objects.filter(
                patient__in=user.responsible.patient_set.all()
            ).order_by('id')
        elif hasattr(user, 'employee'):
            queryset = AppointmentRequest.objects.all(
            ).order_by('id')
        else:
            queryset = AppointmentRequest.objects.none()
        return queryset

    def get_queryset(self):
        return self.prepare_queryset(self.request)


class RequestCreateView(LoginRequiredMixin, CreateView):
    model = AppointmentRequest
    template_name = 'appointments/request_form.html'
    fields = [
        'speciality',
        'doctor',
        'patient',
        'shift',
        'day',
    ]

    def get_success_url(self, **kwargs):
        success_create_url = reverse(
            viewname='appointments:list_requests',
        )

        return success_create_url


class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = AppointmentRequest
    template_name = 'appointments/request_form.html'
    fields = [
        'speciality',
        'doctor',
        'patient',
        'shift',
        'day',
    ]

    def get_success_url(self, **kwargs):
        success_update_url = reverse(
            viewname='appointments:list_requests',
        )

        return success_update_url

    def get_object(self):
        request = AppointmentRequest.objects.get(
            pk=self.kwargs.get('request_pk')
        )
        return request


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = AppointmentRequest
    template_name = 'appointments/request_confirm_delete.html'
    fields = ['speciality',
              'doctor',
              'patient',
              'shift',
              'day',
    ]

    def get_success_url(self, **kwargs):
        success_delete_url = reverse(
            viewname='appointments:list_requests',
        )

        return success_delete_url

    def get_object(self):
        request = AppointmentRequest.objects.get(
            pk=self.kwargs.get('request_pk')
        )
        return request
