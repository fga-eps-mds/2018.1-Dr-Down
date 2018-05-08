from drdown.users.models.model_health_team import HealthTeam
from ..models.model_medical_record import MedicalRecord
from ..models.model_static_data import StaticData
from ..models.model_specific_exams import SpecificExam
from ..models.model_medicines import Medicine
from ..models.model_exams import Exam
from ..models.model_complaint import Complaint
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from search_views.filters import BaseFilter
from ..forms.medicalrecords_forms import MedicalRecordForm
from ..views.views_base import BaseViewForm, BaseViewUrl


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
    slug_url_kwarg = 'username'
    slug_field = 'patient__user__username'
    ordering = ['-day']

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

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        patient = Patient.objects.get(
            user__username=self.kwargs.get('username')
        )

        staticdata = StaticData.objects.filter(patient=patient)
        specificexams = SpecificExam.objects.filter(patient=patient)
        medicines = Medicine.objects.filter(patient=patient)
        exams = Exam.objects.filter(patient=patient)
        complaints = Complaint.objects.filter(patient=patient)

        context['complaints'] = complaints
        context['exams'] = exams
        context['medicines'] = medicines
        context['specificexams'] = specificexams
        context['staticdata'] = staticdata
        context['medicalrecordlist'] = context['object_list']
        context['related_patient'] = patient

        return context


class MedicalRecordsCreateView(BaseViewUrl, BaseViewForm, CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'
