from drdown.users.models.model_health_team import HealthTeam
from ..models.model_medical_record import MedicalRecord
from ..models.model_static_data import StaticData
from ..models.model_medicines import Medicine
from ..models.model_exams import Exam
from ..models.model_risk import Risk
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
        medicines = Medicine.objects.filter(patient=patient)
        complaints = Complaint.objects.filter(patient=patient)
        risk = Risk.objects.filter(patient=patient)

        curves = patient.curves_set.all().order_by('age')

        context['complaints'] = complaints
        context['curves'] = curves
        context['medicines'] = medicines
        context['staticdata'] = staticdata

        context['risk_priority_speech_theraphy'] = \
            patient.risk.get_priority_speech_theraphy_display()
        context['risk_priority_general_practitioner'] = \
            patient.risk.get_priority_general_practitioner_display()
        context['risk_priority_pediatrics'] = \
            patient.risk.get_priority_pediatrics_display()
        context['risk_priority_neurology'] = \
            patient.risk.get_priority_neurology_display()
        context['risk_priority_cardiology'] = \
            patient.risk.get_priority_cardiology_display()
        context['risk_priority_physiotherapy'] = \
            patient.risk.get_priority_physiotherapy_display()
        context['risk_priority_psychology'] = \
            patient.risk.get_priority_psychology_display()

        context['medicalrecordlist'] = context['object_list'].filter(
            patient=patient
        )

        context['related_patient'] = patient

        exams = Exam.objects.filter(patient=patient)
        context['exams'] = exams

        category_dict = {}

        for category in Exam.CATEGORIES:
            query = Exam.objects.filter(
                patient=patient,
                category=category[0]
            )

            if query.exists():
                category_dict[category[1]] = query

        context['exams_categories'] = category_dict

        return context


class MedicalRecordsCreateView(BaseViewUrl, BaseViewForm, CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'
