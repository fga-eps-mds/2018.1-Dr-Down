from drdown.users.models.model_health_team import HealthTeam
from ..models.model_complaint import Complaint
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from django.urls import reverse_lazy
from ..forms.complaint_forms import ComplaintForm
from ..views.views_base import BaseViewForm, BaseViewUrl


class ComplaintCreateView(BaseViewForm, BaseViewUrl, CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'medicalrecords/medicalrecord_complaint_form.html'


class ComplaintUpdateView(BaseViewUrl, UpdateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'medicalrecords/medicalrecord_complaint_form.html'
