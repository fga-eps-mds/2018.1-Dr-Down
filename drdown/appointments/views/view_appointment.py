from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.dates import MonthArchiveView
from drdown.appointments.models import Appointment
from ..forms.appointments_form import AppointmentSearchForm
from django.utils import timezone
from django.urls import reverse


class AppointmentFilter(BaseFilter):
    search_fields = {
        'search_date': ['date_time'],
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
            date = appointment.date_time.year
            if date < first:
                first = date
            if date > last:
                last = date

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
    template_name = 'appointments/form_appointment.html'
    fields = ['speciality',
              'shift',
              'doctor',
              'patient',
              'date_time',
              'motive', ]

    def get_success_url(self, **kwargs):
        success_create_url = reverse(
            viewname='appointments:list_appointments',
        )

        return success_create_url


class AppointmentMonthArchiveView(MonthArchiveView):
    date_field = "date_time"
    allow_future = True
    template_name = 'appointments/appointment_list.html'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(AppointmentMonthArchiveView, self).get_context_data(**kwargs)
        return AppointmentListView.prepare_context(context)

    def get_queryset(self):
        return AppointmentListView.prepare_queryset(self.request)
