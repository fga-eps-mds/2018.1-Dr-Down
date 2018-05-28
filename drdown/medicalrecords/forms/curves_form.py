from django import forms
from drdown.medicalrecords.models.model_curves import (
    Height,
    Weight,
    CephalicPerimeter,
)


class HeightForm(forms.ModelForm):

    class Meta:
        model = Height
        fields = ["height", "age" ]


class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        fields = ["weight", "age" ]


class CephalicPerimeterForm(forms.ModelForm):

    class Meta:
        model = CephalicPerimeter
        fields = ["cephalic_perimeter", "age"]
