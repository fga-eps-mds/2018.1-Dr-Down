from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.appointments.models.model_request import AppointmentRequest
from django.utils.translation import ugettext_lazy as _


class RequestSearchForm(forms.Form):

    search_speciality = forms.ChoiceField(
       required=False,
       label=_('Speciality'),
    )

    search_name = forms.CharField(
       required=False,
       label=_('Name'),
    )

class RequestForm(forms.ModelForm):
    class Meta:
        model = AppointmentRequest
        fields = ('speciality',
                  'doctor',
                  'patient',
                  'shift',
                  'day',
                  'motive',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = HealthTeam.objects.none()

        if 'speciality' in self.data:
            try:
                speciality_id = self.data.get('speciality')
                self.fields['doctor'].queryset = HealthTeam.objects.filter(
                    speciality=speciality_id).order_by('id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields[
                'doctor'].queryset = self.instance.appointment.health_team_set.order_by(
                'id')
