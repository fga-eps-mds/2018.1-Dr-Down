from drdown.users.models.model_health_team import HealthTeam
from ..models.model_specific_exams import SpecificExam
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from django.urls import reverse_lazy
from ..forms.specific_exams_forms import SpecificExamsForm


class SpecificExamCreateView(CreateView):
    model = SpecificExam
    form_class = SpecificExamsForm
    template_name = 'medicalrecords/medicalrecord_specific_exams_form.html'

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
        return super(SpecificExamCreateView, self).form_valid(form)


class SpecificExamUpdateView(UpdateView):
    model = SpecificExam
    form_class = SpecificExamsForm
    template_name = 'medicalrecords/medicalrecord_specific_exams_form.html'

    def get_success_url(self, **kwargs):
        success_update_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_update_url
