from drdown.medicalrecords.models.model_medical_record import MedicalRecord
from django import forms
from pagedown.widgets import PagedownWidget


class MedicalRecordForm(forms.ModelForm):

    message = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = MedicalRecord
        fields = ["message", "document"]
