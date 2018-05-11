from drdown.medicalrecords.models.model_medicines import Medicine
from django import forms


class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ["medicine_name", "medicine_dosage", "medicine_in_use"]
