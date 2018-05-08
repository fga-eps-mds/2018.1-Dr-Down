from drdown.users.models.model_health_team import HealthTeam
from ..models.model_specific_exams import SpecificExam
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from django.urls import reverse_lazy
from ..forms.specific_exams_forms import SpecificExamsForm
from ..views.views_base import BaseViewForm, BaseViewUrl


class SpecificExamCreateView(BaseViewForm, BaseViewUrl, CreateView):
    model = SpecificExam
    form_class = SpecificExamsForm
    template_name = 'medicalrecords/medicalrecord_specific_exams_form.html'


class SpecificExamUpdateView(BaseViewUrl, UpdateView):
    model = SpecificExam
    form_class = SpecificExamsForm
    template_name = 'medicalrecords/medicalrecord_specific_exams_form.html'
    slug_url_kwarg = 'username'
    slug_field = 'patient__user__username'