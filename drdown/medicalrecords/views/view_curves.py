from ..models.model_curves import Curves
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from ..forms.curves_form import CurvesForm
from ..views.views_base import BaseViewUrl, BaseViewPermissions


class FormValid():

    def form_valid(self, form):

        form.instance.patient = Patient.objects.get(
            user__username=self.kwargs.get('username')
        )

        form.save()

        return super().form_valid(form)


class CurvesCreateView(
    FormValid, BaseViewPermissions, BaseViewUrl, CreateView
):
    model = Curves
    form_class = CurvesForm
    template_name = 'medicalrecords/medicalrecord_curves_form.html'


class CurvesUpdateView(
    BaseViewPermissions, BaseViewUrl, UpdateView
):
    model = Curves
    form_class = CurvesForm
    template_name = 'medicalrecords/medicalrecord_curves_form.html'
