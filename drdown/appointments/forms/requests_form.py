from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class RequestSearchForm(forms.Form):
    search_speciality = forms.CharField(
        required=False,
        label=_('Speciality'),
        widget=forms.TextInput(
            attrs={'placeholder': _('Speciality')}
        )
    )

    search_status = forms.CharField(
        required=False,
        label=_('Status'),
        widget=forms.TextInput(
            attrs={'placeholder': _('Status')}
        )
    )

    search_doctor = forms.ModelChoiceField(
        queryset=HealthTeam.objects.all(),
        required=False,
        label=_('Doctor')
    )

    search_patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required=False,
        label=_('Patient')
    )
