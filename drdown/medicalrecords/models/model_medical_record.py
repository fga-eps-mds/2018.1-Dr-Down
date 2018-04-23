from django.db import models
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError


class MedicalRecord(models.Model):

    day = models.DateTimeField(
        _('Created at'),
        help_text=_('Patient Care Day'),
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

    def clean(self, *args, **kwargs):
        if self.day.replace(tzinfo=None)> datetime.now().replace(tzinfo=None):
            raise ValidationError(
                _("You can not create a medical record "
                  "with a date in the future !!"))


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
