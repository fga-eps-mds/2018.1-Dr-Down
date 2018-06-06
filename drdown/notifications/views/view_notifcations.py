from django.views.generic import TemplateView
from drdown.appointments.models.model_request import AppointmentRequest
from drdown.appointments.models.model_appointment import Appointment
from drdown.events.models.model_events import Events
from datetime import timedelta
from django.utils import timezone


class PatientNotificationsView(TemplateView):
    template_name = 'notifications/patient_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(PatientNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        context['scheduled'] = AppointmentRequest.objects.filter(
            status=Appointment.SCHEDULED,
        ).filter(
            patient=user.patient,
        )

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        return context


class ResponsibleNotificationsView(TemplateView):
    template_name = 'notifications/responsible_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(ResponsibleNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        context['appointments'] = Appointment.objects.filter(
            patient__in=user.responsible.patient_set.all(),
        )

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        return context


class HealthTeamNotificationsView(TemplateView):
    template_name = 'notifications/health_team_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(HealthTeamNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        context['appointments'] = Appointment.objects.filter(
            doctor=user.doctor,
        )

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        return context


class EmployeeNotificationsView(TemplateView):
    template_name = 'notifications/employee_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(EmployeeNotificationsView, self).get_context_data(**kwargs)

        context['requests'] = AppointmentRequest.objects.all()

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        return context
