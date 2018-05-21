from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from django.views.generic import UpdateView
from ..models.model_risk import Risk
from ..forms.risk_forms import RiskForm
from ..views.views_base import BaseViewForm, BaseViewUrl, BaseViewPermissions


class RiskUpdateView(BaseViewUrl, UpdateView):
    model = Risk
    form_class = RiskForm
    template_name = 'medicalrecords/risk_form.html'
    slug_url_kwarg = 'username'
    slug_field = 'patient__user__username'
