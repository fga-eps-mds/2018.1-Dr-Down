from drdown.users.models.model_health_team import HealthTeam
from ..models.model_curves import Height, Weight, Curves
from drdown.users.models.model_user import User
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView
from django.urls import reverse_lazy
from ..forms.curves_form import HeightForm, WeightForm, CephalicPerimeterForm
from ..views.views_base import BaseViewForm, BaseViewUrl, BaseViewPermissions

class FormValid():

    def form_valid(self, form):

        form.instance.curves = Curves.objects.get(
            patient__user__username=self.kwargs.get('username')
        )

        form.save()

        return super().form_valid(form)


class HeightCreateView(FormValid, BaseViewPermissions, BaseViewUrl, CreateView):
    model = Height
    form_class = HeightForm
    template_name = 'medicalrecords/medicalrecord_height_form.html'

class HeightUpdateView(BaseViewPermissions, BaseViewUrl, UpdateView):
    model = Height
    form_class = HeightForm
    template_name = 'medicalrecords/medicalrecord_height_form.html'


class WeightCreateView(FormValid, BaseViewPermissions, BaseViewUrl, CreateView):
    model = Weight
    form_class = WeightForm
    template_name = 'medicalrecords/medicalrecord_weight_form.html'


class WeightUpdateView(BaseViewPermissions, BaseViewUrl, UpdateView):
    model = Weight
    form_class = WeightForm
    template_name = 'medicalrecords/medicalrecord_weight_form.html'

class CephalicPerimeterCreateView(FormValid, BaseViewPermissions, BaseViewUrl, CreateView):
    model = Weight
    form_class = CephalicPerimeterForm
    template_name = 'medicalrecords/medicalrecord_cephalic_perimeter_form.html'


class CephalicPerimeterUpdateView(BaseViewPermissions, BaseViewUrl, UpdateView):
    model = Weight
    form_class = CephalicPerimeterForm
    template_name = 'medicalrecords/medicalrecord_cephalic_perimeter_form.html'


