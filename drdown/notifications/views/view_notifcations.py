from django.views.generic import TemplateView
from drdown.appointments.models.model_request import AppointmentRequest
from drdown.appointments.models.model_appointment import Appointment
from drdown.events.models.model_events import Events
from drdown.forum.models.model_post import Post
from drdown.users.models.model_patient import Patient
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.mixins import UserPassesTestMixin


class PatientNotificationsView(UserPassesTestMixin,TemplateView):
    template_name = 'notifications/patient_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(PatientNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        context['scheduled'] = AppointmentRequest.objects.filter(
            status=Appointment.SCHEDULED,
        ).filter(
            patient=user.patient,
        )

        context['cancel'] = AppointmentRequest.objects.filter(
            status=AppointmentRequest.DECLINED,
        ).filter(
            patient=user.patient,
        )

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        post = Post.objects.filter(
            created_by=user
        ).order_by('-created_at').first()
        if post != None:
            context['commentaries'] = post.commentaries.all()

        return context

    def test_func(self):
        return hasattr(self.request.user, 'patient')


class ResponsibleNotificationsView(UserPassesTestMixin,TemplateView):
    template_name = 'notifications/responsible_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(ResponsibleNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        patients = user.responsible.patient_set.all()

        patients_dict_schedule = {}
        patients_dict_cancel = {}

        for patient in patients:
            query_scheduled = AppointmentRequest.objects.filter(
                patient=patient,
                status=AppointmentRequest.SCHEDULED,
            )

            query_cancel = AppointmentRequest.objects.filter(
                patient=patient,
                status=AppointmentRequest.DECLINED,
            )


            patients_dict_schedule[patient.user.name] = query_scheduled
            patients_dict_cancel[patient.user.name] = query_cancel

        context['patients_list_schedule'] = patients_dict_schedule
        context['patients_list_cancel'] = patients_dict_cancel

        context['patients'] = patients

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        post = Post.objects.filter(
            created_by=user
        ).order_by('-created_at').first()
        if post != None:
            context['commentaries'] = post.commentaries.all()

        return context

    def test_func(self):
        return hasattr(self.request.user, 'responsible')


class HealthTeamNotificationsView(UserPassesTestMixin,TemplateView):
    template_name = 'notifications/health_team_notifications.html'

    def get_context_data(self, **kwargs):

        context = super(HealthTeamNotificationsView, self).get_context_data(**kwargs)

        user = self.request.user
        post = Post.objects.filter(
            created_by=user
        ).order_by('-created_at').first()
        if post != None:
            context['commentaries'] = post.commentaries.all()

        start_date = timezone.now()
        end_date = start_date + timedelta(days=6)
        context['events'] = Events.objects.filter(
            date__range=(start_date, end_date)
        )

        context['appointments'] = Appointment.objects.filter(
            doctor=user.healthteam
        ).filter(
            date__day=start_date.date().day
        )

        return context

    def test_func(self):
        return hasattr(self.request.user, 'healthteam')


class EmployeeNotificationsView(UserPassesTestMixin,TemplateView):
    template_name = 'notifications/employee_notifications.html'


    def get_context_data(self, **kwargs):

        context = super(EmployeeNotificationsView, self).get_context_data(**kwargs)

        context['requests'] = AppointmentRequest.objects.filter(
            status=AppointmentRequest.PENDING
        )
        user = self.request.user

        post = Post.objects.filter(
            created_by=user
        ).order_by('-created_at').first()
        if post != None:
            context['commentaries'] = post.commentaries.all()


        return context

    def test_func(self):
        return hasattr(self.request.user, 'employee')
