from django.db import models
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class MedicalRecord(models.Model):

    day = models.DateTimeField(
        _('Created at'),
        help_text=_('Patient Care Day'),
        auto_now_add=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    message = models.TextField(
        _('Message'),
        help_text=_('Message of post'),
        max_length=4000
    )
