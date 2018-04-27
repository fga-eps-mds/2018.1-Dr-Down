from django.db import models
from drdown.users.models import User
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError


class MedicalRecord(models.Model):

    document = models.FileField(upload_to='media/', blank=True)

    day = models.DateTimeField(
        _('Created at'),
        help_text=_('Patient Care Day'),
        auto_now=True
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

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
    )

    class Meta:
        verbose_name = _("Medical Record")
        verbose_name_plural = _("Medical Records")
