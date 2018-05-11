from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_health_team import HealthTeam

from django.urls import reverse_lazy


class BaseViewForm():

    def form_valid(self, form):

        form.instance.patient = Patient.objects.get(
            user__username=self.kwargs.get('username')
        )

        form.instance.author = self.request.user.healthteam
        form.save()

        return super().form_valid(form)


class BaseViewUrl():

    def get_success_url(self, **kwargs):

        success_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username')
            }
        )

        return success_url
