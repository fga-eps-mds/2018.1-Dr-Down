from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class RequestSearchForm(forms.Form):

    search_speciality = forms.ChoiceField(
       required=False,
       label=_('Speciality'),
    )

    search_name = forms.CharField(
       required=False,
       label=_('Name'),
    )
