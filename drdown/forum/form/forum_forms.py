from drdown.medicalrecords.models.model_medical_record import MedicalRecord
from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.forum.models.model_commentary import Commentary
from pagedown.widgets import PagedownWidget

class ComentaryForm(forms.ModelForm):

    message = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Commentary
        fields = ["message"]
