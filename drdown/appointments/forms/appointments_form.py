from drdown.appointments.models.model_appointment import Appointment
from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class AppointmentSearchForm(forms.Form):
    search_speciality = forms.CharField(
        required=False,
        label=_('Speciality'),
        widget=forms.TextInput(
            attrs={'placeholder': _('Speciality')}
        )
    )

    search_date = forms.DateField(
        required=False,
        label=_('Date'),
        widget=forms.TextInput(
            attrs={'placeholder': _('(Year)-(Month)-(Day)')}
        )
    )

    search_doctor = forms.ModelChoiceField(
        queryset=HealthTeam.objects.all(),
        required=False,
        label=_('Doctor')
    )

    search_patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required=False,
        label=_('Patient')
    )
