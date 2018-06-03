from django.views.generic import TemplateView
from drdown.appointments.models.model_appointment import Appointment


class NotificationCenterView(TemplateView):
    template_name = 'notifications/notifications.html'

    def get_context_data(self, **kwargs):
        context = super(NotificationCenterView, self).get_context_data(**kwargs)
        user = self.request.user

        if hasattr(user, 'patient'):
            context['appointments'] = Appointment.objects.filter(
                patient=user.patient,
            )

        return context
