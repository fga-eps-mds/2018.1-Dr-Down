from drdown.users.models.model_health_team import HealthTeam
from ..models.model_exams import Exam
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from django.urls import reverse_lazy
from ..forms.exam_forms import ExamForm
from ..views.views_base import BaseViewForm, BaseViewUrl, BaseViewPermissions


class ExamCreateView(BaseViewForm, BaseViewUrl, BaseViewPermissions,
                     CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'medicalrecords/medicalrecord_exam_form.html'


class ExamUpdateView(BaseViewUrl, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'medicalrecords/medicalrecord_exam_form.html'
