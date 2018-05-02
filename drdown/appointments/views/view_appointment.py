from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.dates import MonthArchiveView
from drdown.appointments.models import Appointment
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from ..forms.appointments_form import AppointmentSearchForm
from django.utils import timezone
from django.urls import reverse


class AppointmentFilter(BaseFilter):
    search_fields = {
        'search_date': ['date'],
        'search_speciality': ['speciality'],
        'search_doctor': ['doctor__id'],
        'search_patient': ['patient__id'],
    }


class AppointmentListView(SearchListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    form_class = AppointmentSearchForm
    filter_class = AppointmentFilter

    @staticmethod
    def get_year_range_of_appointment():
        first = 3000
        last = 0
        for appointment in Appointment.objects.all():
            year = appointment.date.year
            if year < first:
                first = year
            if year > last:
                last = year

        return [first, last]

    @staticmethod
    def get_list_of_years(range_years):
        years = []
        first = range_years[0]
        last = range_years[1]
        if first == last:
            years.append(first)
        else:
            for year in range(first, last + 1):
                years.append(year)
        return years

    @staticmethod
    def prepare_context(context):
        months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        range_years = AppointmentListView.get_year_range_of_appointment()
        context['years'] = AppointmentListView.get_list_of_years(range_years)
        context['months'] = months
        context['current_year'] = timezone.now().year
        return context

    @staticmethod
    def prepare_queryset(request):
        user = request.user
        if hasattr(user, 'patient'):
            queryset = Appointment.objects.filter(
                patient=user.patient
            )
        elif hasattr(user, 'responsible'):
            queryset = Appointment.objects.filter(
                patient=user.responsible.patient
            )
        elif hasattr(user, 'employee'):
            queryset = Appointment.objects.all()
        elif hasattr(user, 'healthteam'):
            queryset = Appointment.objects.filter(
                doctor=user.healthteam
            )
        else:
            queryset = Appointment.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        return self.prepare_context(context)

    def get_queryset(self):
        return self.prepare_queryset(self.request)


class AppointmentCreateView(CreateView):
    model = Appointment
    sucess_url = 'appointmentslist_appointments'
    template_name = 'appointments/appointment_form.html'
    fields = [
        'speciality',
        'shift',
        'doctor',
        'patient',
        'date',
        'time',
        'motive',
    ]

    def get_success_url(self, **kwargs):
        print("Entra em get_success_url")
        success_create_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_create_url

    def form_valid(self, form):
        form.save()
        return super(AppointmentCreateView, self).form_valid(form)

    @staticmethod
    def get_health_team():
        health_team = []

        for doctor in HealthTeam.objects.all():
            health_team.append(doctor)

        return health_team

    @staticmethod
    def get_patients():
        patients = []

        for patient in Patient.objects.all():
            patients.append(patient)

        return patients

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)

        context['health_team'] = self.get_health_team()
        context['patients'] = self.get_patients()
        return context


class AppointmentMonthArchiveView(MonthArchiveView):
    date_field = "date"
    allow_future = True
    template_name = 'appointments/appointment_list.html'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(AppointmentMonthArchiveView,
                        self).get_context_data(**kwargs)
        return AppointmentListView.prepare_context(context)

    def get_queryset(self):
        return AppointmentListView.prepare_queryset(self.request)


class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['speciality',
              'shift',
              'doctor',
              'patient',
              'date_time',
              'motive', ]

    def get_object(self):
        appointment = Appointment.objects.get(
            pk=self.kwargs.get('appointment_pk')
        )
        return appointment

    def get_context_data(self, **kwargs):
        context = super(AppointmentUpdateView, self).get_context_data(**kwargs)

        context['health_team'] = AppointmentCreateView.get_health_team()
        context['patients'] = AppointmentCreateView.get_patients()
        return context
