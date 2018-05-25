from drdown.appointments.models.model_appointment import Appointment
from django import forms
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class AppointmentSearchForm(forms.Form):
    search_speciality = forms.ChoiceField(
        required=False,
        label=_('Speciality'),
    )

    search_date = forms.DateField(
        required=False,
        label=_('Date'),
        widget=forms.SelectDateWidget(
            empty_label=(_("Year"), _("Month"), _("Day")),
        )
    )

    search_doctor = forms.CharField(
        required=False,
        label=_('Doctor'),
    )

    search_patient = forms.CharField(
        required=False,
        label=_('Patient'),
    )
