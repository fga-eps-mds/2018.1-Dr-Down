from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import DetailView
from ..views.views_base import BaseViewPermissionPatientResponsible


class PDFView(
    BaseViewPermissionPatientResponsible, DetailView
):

    model = Patient
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    template_name = 'medicalrecords/medicalrecord_pdf.html'
