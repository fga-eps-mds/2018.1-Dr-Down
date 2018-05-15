from drdown.medicalrecords.models.model_medicines import Medicine
from django import forms


class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = [
            "medicine_name",
            "medicine_dosage",
            "medicine_use_interval",
            "medicine_in_use",
        ]
