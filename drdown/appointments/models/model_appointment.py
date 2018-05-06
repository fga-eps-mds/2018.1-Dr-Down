from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class Appointment(models.Model):

    date = models.DateField(
        _('Date'),
        help_text=_('Date of appointment'),
        max_length=50
    )

    time = models.TimeField(
        _('Time'),
        help_text=_('Time of appointment'),
        max_length=50
    )

    SPEECH_THERAPHY = "Speech Therapy"
    PSYCHOLOGY = "Psychology"
    PHYSIOTHERAPY = "Physiotherapy"
    OCCUPATIONAL_THERAPY = "Occupational Therapy"
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    PEDIATRICS = "Pediatrics"

    SPECIALITY_APPOINTMENT_CHOICES = (
        (SPEECH_THERAPHY, _('Speech Therapy')),
        (PSYCHOLOGY, _('Psychology')),
        (PHYSIOTHERAPY, _('Physiotherapy')),
        (OCCUPATIONAL_THERAPY, _('Occupational Therapy')),
        (CARDIOLOGY, _('Cardiology')),
        (NEUROLOGY, _('Neurology')),
        (PEDIATRICS, _('Pediatrics')),
    )

    speciality = models.CharField(
        _('Speciality'),
        choices=SPECIALITY_APPOINTMENT_CHOICES,
        help_text=_("Speciality of appointment"),
        max_length=30
    )

    doctor = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_('Doctor'),
        related_name='appointments',
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient'),
        related_name='appointments',
    )

    SCHEDULED = 'Scheduled'
    CANCELED = 'Canceled'
    DONE = 'Done'

    STATUS_CHOICES = (
        (SCHEDULED, _('Scheduled')),
        (CANCELED, _('Canceled')),
    )

    status = models.CharField(
        _('Status'),
        choices=STATUS_CHOICES,
        help_text=_("Is this appointment still scheduled?"),
        default=SCHEDULED,
        max_length=20,
        editable=False,
    )

    def __str__(self):
        return _('Appointment of ') + self.patient.user.name

    class Meta:
        verbose_name = _("Appointment")
        verbose_name_plural = _("Appointments")
