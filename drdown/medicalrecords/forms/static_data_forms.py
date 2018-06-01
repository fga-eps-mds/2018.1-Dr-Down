from drdown.medicalrecords.models.model_static_data import StaticData
from django import forms


class StaticDataForm(forms.ModelForm):

    class Meta:
        model = StaticData
        fields = ["weight", "APGAR", "heart_test", "ear_test", "foot_test"]
