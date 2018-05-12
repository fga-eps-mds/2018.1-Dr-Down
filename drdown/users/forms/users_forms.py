from django import forms
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class PatientSearchForm(forms.Form):

    list_patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required=False,
        label=_('Search patient!')
    )
