from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError


class StaticData(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    weight = models.IntegerField(
        verbose_name=_('Weight at birth'),
        help_text=_('In grams')
    )

    APGAR = models.IntegerField(
        choices=list(zip(range(1, 11), range(1, 11))),
    )

    heart_test = models.FileField(
        upload_to='media/medicalrecords',
        blank=True,
        verbose_name=_('Heart Test')
    )

    ear_test = models.FileField(
        upload_to='media/medicalrecords',
        blank=True,
        verbose_name=_('Test of the Ear')
    )

    author = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
    )

    class Meta:
        verbose_name = _("Medical Record Static Data")
