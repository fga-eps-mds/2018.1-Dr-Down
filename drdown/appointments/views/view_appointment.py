from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from drdown.appointments.models import Appointment
from django.utils import timezone
from django.urls import reverse


class AppointmentListView(ListView):
    model = Appointment

    def get_year_range_of_appointment(self):
        first = 3000
        last = 0
        for appointment in Appointment.objects.all():
            date = appointment.date_time.year
            if date < first:
                first = date
            if date > last:
                last = date

        return [first, last]

    def get_list_of_years(self, range_years):
        years = []
        first = range_years[0]
        last = range_years[1]
        if first == last:
            years.append(first)
        else:
            for year in range(first, last + 1):
                years.append(year)
        return years

    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
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
        range_years = self.get_year_range_of_appointment()
        context['years'] = self.get_list_of_years(range_years)
        context['months'] = months
        context['current_year'] = timezone.now().year
        return context


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
