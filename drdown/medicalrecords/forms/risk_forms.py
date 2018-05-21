from drdown.medicalrecords.models.model_risk import Risk
from django import forms


class RiskForm(forms.ModelForm):

    class Meta:
        model = Risk
        fields = ["priority_speech_theraphy", "priority_psychology",
         "priority_physiotherapy", "priority_cardiology", "priority_neurology",
          "priority_pediatrics", "priority_general_practitioner"]
