from django.views.generic import TemplateView
from drdown.appointments.models.model_appointment import Appointment
from drdown.events.models.model_events import Events
from datetime import  timedelta
from django.utils import timezone


class PatientNotificationsView(TemplateView):
    template_name = 'notifications/patient_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(PatientNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        context['appointments'] = Appointment.objects.filter(
            patient=user.patient,
        )

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range= (start_date, end_date)
        )

        return context
