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


class PatientSearchForm(forms.Form):

    list_patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required=False,
        label=_('Search patient!')
    )
