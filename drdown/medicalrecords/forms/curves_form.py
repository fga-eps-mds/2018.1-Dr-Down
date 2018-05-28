from drdown.medicalrecords.models.model_curves import Height, Weight
from django import forms


class HeightForm(forms.ModelForm):

    class Meta:
        model = Height
        fields = ["height", "age" ]


class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        fields = ["weight", "age" ]