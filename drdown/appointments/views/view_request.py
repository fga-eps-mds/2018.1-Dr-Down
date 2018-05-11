from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from drdown.appointments.models import AppointmentRequest
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

    def prepare_queryset(self, request):
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
        'motive',
    ]
    success_url = reverse_lazy(
            viewname='appointments:list_requests',
    )


class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = AppointmentRequest
    template_name = 'appointments/request_form.html'
    fields = [
        'speciality',
        'doctor',
        'patient',
        'shift',
        'day',
        'motive',
    ]
    success_url = reverse_lazy(
            viewname='appointments:list_requests',
    )
    pk_url_kwarg = 'request_pk'


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = AppointmentRequest
    template_name = 'appointments/request_confirm_delete.html'
    success_url = reverse_lazy(
            viewname='appointments:list_requests',
    )
    pk_url_kwarg = 'request_pk'


class RequestUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = AppointmentRequest
    template_name = 'appointments/request_confirm_cancel.html'
    fields = ['observation']
    success_url = reverse_lazy(
            viewname='appointments:list_requests',
    )
    pk_url_kwarg = 'request_pk'

    def form_valid(self, form):
        form.instance.status = AppointmentRequest.DECLINED
        form.save()
        return super(RequestUpdateStatusView, self).form_valid(form)


class RequestAfterResultDeleteView(LoginRequiredMixin, DeleteView):
    model = AppointmentRequest
    template_name = 'appointments/request_after_result_confirm_delete.html'
    success_url = reverse_lazy(
            viewname='appointments:list_requests',
    )
    pk_url_kwarg = 'request_pk'
