from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import DetailView
from ..views.views_base import BaseViewPermissions


class PDFView(
    BaseViewPermissions, DetailView
):

    model = Patient
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    template_name = 'medicalrecords/medicalrecord_pdf.html'

    def test_func(self):
        return super().test_func() or \
            self.request.user.username == self.kwargs.get('username') or \
            (
                hasattr(self.request.user, 'responsible') and
                self.request.user.responsible.patient_set.filter(
                    user__username=self.kwargs.get('username')
                )
            )
