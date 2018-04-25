from drdown.medicalrecords.models.model_medical_record import MedicalRecord
from django import forms


class MedicalRecordSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search patient!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )
