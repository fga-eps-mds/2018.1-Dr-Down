from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Complaint(models.Model):

    created_at = models.DateTimeField(
        _('Created at'),
        help_text=_('Date of creation'),
        auto_now_add=True
    )

    complaint_day = models.DateField(
        _('Day of complaint'),
    )

    complaint_time = models.TimeField(
        _('Time of complaint'),
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    description = models.TextField(
        _('Description'),
        help_text=_('Description of the complaint'),
        max_length=4000
    )

    author = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
    )

    class Meta:
        verbose_name = _("Complaint")
        verbose_name_plural = _("Complaints")

    def __str__(self):
        return self.patient.user.get_username() + " -  Comptaint ID: " + \
               str(self.id)
