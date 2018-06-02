from django import forms
from drdown.medicalrecords.models.model_curves import (
    Curves
)


class CurvesForm(forms.ModelForm):

    class Meta:
        model = Curves
        fields = ["height", "weight", "age", "cephalic_perimeter", ]
