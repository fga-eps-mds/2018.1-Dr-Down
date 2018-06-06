from django import forms
from drdown.medicalrecords.models.model_curves import (
    Curves
)


class CurvesForm(forms.ModelForm):

    weight = forms.FloatField(min_value=0.0)

    height = forms.IntegerField(min_value=0)

    cephalic_perimeter = forms.FloatField(min_value=0.0)

    age = forms.IntegerField(min_value=0)

    class Meta:
        model = Curves
        fields = ["height", "weight", "age", "cephalic_perimeter", ]
