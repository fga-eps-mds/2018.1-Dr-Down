from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class Medicine(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    medicine_name = models.CharField(
        max_length=100,
        verbose_name=_('Medicine Name')
    )

    medicine_dosage = models.CharField(
        max_length=100,
        verbose_name=_('Medicine dosage')
    )

    medicine_in_use = models.BooleanField(
        verbose_name=_('In use?'),
        help_text=_('Does the patient still use this medication?'),
        default=True
    )

    medicine_use_interval = models.CharField(
        _('Time between uses'),
        max_length=50,
        default=""
    )

    author = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
    )

    def __str__(self):
        return self.patient.user.get_username() + " - " + self.medicine_name

    class Meta:
        verbose_name = _("Patient Medicine")
