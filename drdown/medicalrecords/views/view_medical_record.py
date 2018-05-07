from drdown.users.models.model_health_team import HealthTeam
from ..models.model_medical_record import MedicalRecord
from ..models.model_static_data import StaticData
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from search_views.filters import BaseFilter
from ..forms.medicalrecords_forms import MedicalRecordForm


class MedicalRecordsFilter(BaseFilter):
    search_fields = {
        'list_patient': ['id']
    }


class CheckPermissions(UserPassesTestMixin):
    def test_func(self):
        return hasattr(self.request.user, 'healthteam') or \
               hasattr(self.request.user, 'employee')

    def get_login_url(self):
        if self.request.user.is_authenticated:
            # redirect if user is not a HealthTeam
            login_url = reverse_lazy(
                viewname='users:detail',
                kwargs={'username': self.request.user.username}
            )
            return login_url
        login_MedicalRecordsList_url = reverse_lazy('account_login')
        return login_MedicalRecordsList_url


class MedicalRecordsList(UserPassesTestMixin, ListView):
    model = MedicalRecord
    template_name = "medicalrecords/medicalrecord_list.html"

    def test_func(self):
        return hasattr(self.request.user, 'healthteam') or \
               hasattr(self.request.user, 'employee') or \
               self.request.user.username == self.kwargs.get('username') or \
               (hasattr(self.request.user, 'responsible') and
                self.request.user.responsible.patient_set.filter(
                    user__username=self.kwargs.get('username')))

    def get_login_url(self):
        if self.request.user.is_authenticated:
            # redirect if user is not a HealthTeam or the patient itself
            login_MedicalRecordsList_url = reverse_lazy(
                viewname='users:detail',
                kwargs={'username': self.request.user.username}
            )
            return login_MedicalRecordsList_url
        login_MedicalRecordsList_url = reverse_lazy('account_login')
        return login_MedicalRecordsList_url

    def get_queryset(self):
        queryset = MedicalRecord.objects.all().order_by('-day')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordsList, self).get_context_data(**kwargs)
        patient = Patient.objects.get(
            user__username=self.kwargs.get('username')
        )
        medicalrecordlist = MedicalRecord.objects.filter(patient=patient)
        staticdata = StaticData.objects.get(patient=patient)
        context['medicalrecordlist'] = medicalrecordlist
        context['related_patient'] = patient
        context['staticdata'] = staticdata
        return context


class MedicalRecordsCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'

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
        return super(MedicalRecordsCreateView, self).form_valid(form)


class MedicalRecordsDeleteView(DeleteView):
    model = MedicalRecord

    def get_success_url(self, **kwargs):
        success_delete_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_delete_url


class MedicalRecordsUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'

    def get_success_url(self, **kwargs):
        success_update_url = reverse_lazy(
            viewname='medicalrecords:list_medicalrecords',
            kwargs={
                'username': self.kwargs.get('username'),
            }
        )
        return success_update_url
