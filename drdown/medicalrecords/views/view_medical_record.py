from drdown.users.models.model_health_team import HealthTeam
from ..models.model_medical_record import MedicalRecord
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from search_views.search import SearchListView
from django.contrib.auth.mixins import UserPassesTestMixin
from search_views.filters import BaseFilter
from ..forms.medicalrecords_forms import MedicalRecordSearchForm,\
    MedicalRecordCompleteSearchForm, PatientSearchForm, MedicalRecordForm


class MedicalRecordsFilter(BaseFilter):
    search_fields = {
        'search_text': ['message'],
        'search_date': ['day'],
        'author': ['author_id__id'],
        'patient': ['patient__id'],
        'message': ['message'],
        'list_patient': ['id']
    }


class CheckPermissions(UserPassesTestMixin):
    def test_func(self):
        return hasattr(self.request.user, 'healthteam')

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


class MedicalRecordsList(UserPassesTestMixin, SearchListView):
    model = MedicalRecord
    template_name = "medicalrecords/medicalrecord_list.html"
    form_class = MedicalRecordSearchForm
    filter_class = MedicalRecordsFilter

    def test_func(self):
        return hasattr(self.request.user, 'healthteam') or \
               self.request.user.username == self.kwargs.get('username')

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

    def related_patient(self):
        user = User.objects.get(
            username=self.kwargs.get('username')
        )
        patient = Patient.objects.get(
            user=user
        )
        return patient

    def get_queryset(self):
        queryset = MedicalRecord.objects.all().order_by('-day')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordsList, self).get_context_data(**kwargs)
        elect_count = 0
        for device in MedicalRecord.objects.all():
            if device.patient.user.username == self.kwargs.get('username'):
                elect_count += 1
        context['elect_count'] = elect_count
        return context


class MedicalRecordsSearchList(CheckPermissions, SearchListView):
    model = MedicalRecord
    template_name = "medicalrecords/medicalrecord_search_list.html"
    form_class = MedicalRecordCompleteSearchForm
    filter_class = MedicalRecordsFilter
    paginate_by = 10

    def get_queryset(self):
        queryset = MedicalRecord.objects.all().order_by('-day')
        return queryset


class PatientSearchList(CheckPermissions, SearchListView):
    model = Patient
    template_name = "medicalrecords/medicalrecord_patient_list.html"
    form_class = PatientSearchForm
    filter_class = MedicalRecordsFilter
    paginate_by = 20


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
