from drdown.users.models.model_health_team import HealthTeam
from ..models.model_complaint import Complaint
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from django.urls import reverse_lazy
from ..forms.comlaint_forms import ComplaintForm


class ComplaintCreateView(CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'medicalrecords/medicalrecord_complaint_form.html'

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username')
            }
        )
        return success_create_url

    def form_valid(self, form):
        for patient in Patient.objects.all():
            if patient.user.username == self.kwargs.get('username'):
                form.instance.patient = patient
        user = User.objects.get(
            username=self.request.user
        )
        healthteam = HealthTeam.objects.get(
            user=user
        )
        form.instance.author = healthteam
        form.save()
        return super(ComplaintCreateView, self).form_valid(form)


class ComplaintUpdateView(UpdateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'medicalrecords/medicalrecord_complaint_form.html'

    def get_success_url(self, **kwargs):
        success_update_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_update_url
