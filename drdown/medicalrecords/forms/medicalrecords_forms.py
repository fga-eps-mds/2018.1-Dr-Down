from drdown.medicalrecords.models.model_medical_record import MedicalRecord
from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from pagedown.widgets import PagedownWidget
from django.utils.translation import ugettext_lazy as _


class MedicalRecordForm(forms.ModelForm):

    message = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = MedicalRecord
        fields = ["message", "document"]


class MedicalRecordSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search patient!',
        widget=forms.TextInput(attrs={'placeholder': _('search here!')})
    )

    search_date = forms.DateField(
        required=False,
        label='Search date!',
        widget=forms.TextInput(attrs={'placeholder': '(Year)-(Month)-(Day)'})
    )

    author = forms.ModelChoiceField(
        queryset=HealthTeam.objects.all(),
        required=False,
        label=_('Search author!')
    )


class MedicalRecordCompleteSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label=_('Search patient!'),
        widget=forms.TextInput(attrs={'placeholder': _('search here!')})
    )

    search_date = forms.DateField(
        required=False,
        label=_('Search date!'),
        widget=forms.TextInput(attrs={'placeholder': '(Year)-(Month)-(Day)'})
    )

    author = forms.ModelChoiceField(
        queryset=HealthTeam.objects.all(),
        required=False,
        label=_('Search author!')
    )

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required=False,
        label=_('Search patient!')
    )


class PatientSearchForm(forms.Form):

    list_patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required=False,
        label=_('Search patient!')
    )
