from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from drdown.appointments.models import Appointment
from drdown.appointments.models import AppointmentRequest
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from ..forms.appointments_form import AppointmentSearchForm


class AppointmentFilter(LoginRequiredMixin, BaseFilter):
    search_fields = {
        'search_date': ['date'],
        'search_speciality': ['speciality'],
        'search_doctor': ['doctor__user__name'],
        'search_patient': ['patient__user__name'],
    }


class AppointmentListView(LoginRequiredMixin, SearchListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    form_class = AppointmentSearchForm
    filter_class = AppointmentFilter
    paginate_by = 10

    @staticmethod
    def get_list_of_years(request):
        years = []
        for appointment in AppointmentListView.prepare_queryset(request):
            if appointment.date.year not in years:
                years.append(appointment.date.year)
        years.sort(reverse=True)
        return years

    @staticmethod
    def get_list_of_months(request):
        months = [
            _('January'),
            _('February'),
            _('March'),
            _('April'),
            _('May'),
            _('June'),
            _('July'),
            _('August'),
            _('September'),
            _('October'),
            _('November'),
            _('December'),
        ]

        return months

    @staticmethod
    def prepare_context(context, request):
        context['years'] = AppointmentListView.get_list_of_years(request)
        context['months'] = AppointmentListView.get_list_of_months(request)
        context['current_year'] = timezone.now().year
        context['canceled'] = Appointment.CANCELED
        return context

    @staticmethod
    def prepare_queryset(request):
        user = request.user
        if hasattr(user, 'patient'):
            queryset = Appointment.objects.filter(
                patient=user.patient
            ).order_by('-date', '-time')
        elif hasattr(user, 'responsible'):
            queryset = Appointment.objects.filter(
                patient__in=user.responsible.patient_set.all()
            ).order_by('-date', '-time')
        elif hasattr(user, 'employee'):
            queryset = Appointment.objects.all(
            ).order_by('-date', '-time')
        elif hasattr(user, 'healthteam'):
            queryset = Appointment.objects.filter(
                doctor=user.healthteam
            ).order_by('-date', '-time')
        else:
            queryset = Appointment.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        return self.prepare_context(context, self.request)

    def get_queryset(self):
        return self.prepare_queryset(self.request)


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = [
        'speciality',
        'doctor',
        'patient',
        'date',
        'time',
    ]

    def get_success_url(self, **kwargs):
        success_create_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_create_url

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)

        context['health_team'] = HealthTeam.objects.all()
        context['patients'] = Patient.objects.all()
        return context


class AppointmentMonthArchiveView(LoginRequiredMixin, MonthArchiveView):
    date_field = "date"
    allow_future = True
    template_name = 'appointments/appointment_list.html'
    allow_empty = True
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(AppointmentMonthArchiveView,
                        self).get_context_data(**kwargs)
        return AppointmentListView.prepare_context(context, self.request)

    def get_queryset(self):
        return AppointmentListView.prepare_queryset(self.request)


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = [
        'doctor',
        'patient',
        'date',
        'time',
    ]

    def get_success_url(self, **kwargs):
        success_update_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_update_url

    def get_object(self):
        appointment = Appointment.objects.get(
            pk=self.kwargs.get('appointment_pk')
        )
        return appointment

    def get_context_data(self, **kwargs):
        context = super(AppointmentUpdateView, self).get_context_data(**kwargs)

        context['health_team'] = HealthTeam.objects.all()
        return context


class AppointmentUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_cancel.html'
    fields = []

    def get_success_url(self, **kwargs):
        success_update_status_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_update_status_url

    def get_object(self):
        appointment = Appointment.objects.get(
            pk=self.kwargs.get('appointment_pk')
        )
        return appointment

    def form_valid(self, form):
        form.instance.status = Appointment.CANCELED
        form.save()
        return super(AppointmentUpdateStatusView, self).form_valid(form)


class AppointmentFromRequestCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_request_form.html'
    fields = [
        'speciality',
        'doctor',
        'patient',
        'date',
        'time',
    ]
    success_url = reverse_lazy(
            viewname='appointments:list_appointments',
    )

    def get_context_data(self, **kwargs):
        context = super(
            AppointmentFromRequestCreateView, self).get_context_data(**kwargs)
        test = AppointmentRequest.objects.get(pk=self.kwargs.get('request_pk'))
        context['health_team'] = HealthTeam.objects.filter(speciality=test.speciality)
        context['appointment_request'] = test
        return context


    def form_valid(self, form):
        request = AppointmentRequest.objects.get(
            pk=self.kwargs.get('request_pk')
        )
        request.status = AppointmentRequest.SCHEDULED
        request.save()
        form.save()
        return super(AppointmentFromRequestCreateView, self).form_valid(form)
