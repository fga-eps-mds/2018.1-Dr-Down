from drdown.medicalrecords.models.model_medical_record import MedicalRecord
from django import forms
from drdown.users.models.model_health_team import HealthTeam


class MedicalRecordSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search patient!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )

    search_date = forms.DateField(
        required=False,
        label='Search date!'
    )

    author = forms.ModelChoiceField(
        queryset=HealthTeam.objects.all(),
        required=False,
        label='Search author!'
    )

