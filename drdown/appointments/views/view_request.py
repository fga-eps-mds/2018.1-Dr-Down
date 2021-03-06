from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from search_views.search import SearchListView
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_health_team import HealthTeam
from search_views.filters import BaseFilter
from drdown.appointments.models import AppointmentRequest
from drdown.appointments.forms.requests_form import RequestSearchForm, \
    RequestForm


class RequestFilter(LoginRequiredMixin, BaseFilter):
    search_fields = {
        'search_speciality': ['speciality'],
        'search_name': ['doctor__user__name', 'patient__user__name'],
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
            queryset = AppointmentRequest.objects.filter(
                ).order_by('risk', 'id')
        else:
            queryset = AppointmentRequest.objects.none()
        return queryset

    def get_queryset(self):
        return self.prepare_queryset(self.request)


class RequestCreateView(LoginRequiredMixin, CreateView):
    model = AppointmentRequest
    template_name = 'appointments/request_form.html'
    form_class = RequestForm
    success_url = reverse_lazy(
            viewname='appointments:list_requests',
    )

    def form_valid(self, form):
        speciality = form.instance.speciality
        risk = 5

        if speciality == AppointmentRequest.CARDIOLOGY:
            risk = form.instance.patient.risk.priority_cardiology

        if speciality == AppointmentRequest.NEUROLOGY:
            risk = form.instance.patient.risk.priority_neurology

        if speciality == AppointmentRequest.PEDIATRICS:
            risk = form.instance.patient.risk.priority_pediatrics

        if speciality == AppointmentRequest.SPEECH_THERAPHY:
            risk = form.instance.patient.risk.priority_speech_theraphy

        if speciality == AppointmentRequest.PHYSIOTHERAPY:
            risk = form.instance.patient.risk.priority_physiotherapy

        if speciality == AppointmentRequest.PSYCHOLOGY:
            risk = form.instance.patient.risk.priority_psychology

        if speciality == AppointmentRequest.GENERAL_PRACTITIONER:
            risk = form.instance.patient.risk.priority_general_practitioner

        form.instance.risk = risk

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RequestCreateView, self).get_context_data(**kwargs)

        context['health_team'] = HealthTeam.objects.all()
        if hasattr(self.request.user, 'patient'):
            context['patients'] = Patient.objects.filter(
                user=self.request.user)
        elif hasattr(self.request.user, 'responsible'):
            context['patients'] = \
                self.request.user.responsible.patient_set.all()
        return context


def load_doctors(request):
    speciality = request.GET.get('speciality')
    doctors = HealthTeam.objects.filter(
        speciality=speciality
    ).order_by('user__name')
    return render(request,
                  'appointments/doctors_dropdown_list_options.html',
                  {'doctors': doctors}
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
