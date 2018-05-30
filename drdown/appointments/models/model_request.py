from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class AppointmentRequest(models.Model):

    MORNING = 'M'
    AFTERNOON = 'A'

    SHIFT_CHOICES = (
        (MORNING, _('Morning')),
        (AFTERNOON, _('Afternoon')),
    )

    shift = models.CharField(
        _('Shift'),
        choices=SHIFT_CHOICES,
        help_text=_('Preferred shift'),
        max_length=10
    )

    SUNDAY = 'Sunday'
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'

    DAYS_CHOICES = (
        (SUNDAY, _('Sunday')),
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
    )

    day = models.CharField(
        _('Day of the week'),
        choices=DAYS_CHOICES,
        help_text=_("Preferred day of the week. " +
                    "It is not guaranteed that the appointment will be " +
                    "marked on the preferred day."),
        max_length=10
    )

    motive = models.TextField(
        _('Motive'),
        help_text=_('Why are you requesting an appointment?'),
        max_length=500,
        blank=True,
    )

    observation = models.TextField(
        _('Observation'),
        help_text=_('Why was it scheduled/declined?'),
        max_length=500,
        blank=True,
    )

    SPEECH_THERAPHY = "Speech Therapy"
    PSYCHOLOGY = "Psychology"
    PHYSIOTHERAPY = "Physiotherapy"
    OCCUPATIONAL_THERAPY = "Occupational Therapy"
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    PEDIATRICS = "Pediatrics"
    GENERAL_PRACTITIONER = "General Practitioner"

    SPECIALITY_REQUEST_CHOICES = (
        (SPEECH_THERAPHY, _('Speech Therapy')),
        (PSYCHOLOGY, _('Psychology')),
        (PHYSIOTHERAPY, _('Physiotherapy')),
        (OCCUPATIONAL_THERAPY, _('Occupational Therapy')),
        (CARDIOLOGY, _('Cardiology')),
        (NEUROLOGY, _('Neurology')),
        (PEDIATRICS, _('Pediatrics')),
        (GENERAL_PRACTITIONER, _('General Practitioner')),
    )

    speciality = models.CharField(
        _('Speciality'),
        choices=SPECIALITY_REQUEST_CHOICES,
        help_text=_("Desired specialty"),
        max_length=30
    )

    doctor = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_('Doctor'),
        related_name='requests',
        help_text=_("Preferred doctor. " +
                    "It is not guaranteed that the appointment will be " +
                    "scheduled with the doctor preferred."),
        blank=True,
        null=True,
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient'),
        related_name='requests',
    )

    SCHEDULED = 'Scheduled'
    PENDING = 'Pending'
    DECLINED = 'Declined'

    STATUS_CHOICES = (
        (SCHEDULED, _('Scheduled')),
        (DECLINED, _('Declined')),
    )

    status = models.CharField(
        _('Status'),
        help_text=_("Was the request accepted?"),
        choices=STATUS_CHOICES,
        default=PENDING,
        max_length=20,
        editable=False,
    )

    RISKS = (
      (5, _('Not urgent')),
      (4, _('Not very urgent')),
      (3, _('Urgent')),
      (2, _('Very urgent')),
      (1, _('Emerging')),
    )
    risk = models.IntegerField(
      _('Risk'),
      choices=RISKS,
      default=5,
    )

    def __str__(self):
        return _('Appointment request of ') + self.patient.user.name

    class Meta:
        verbose_name = _("Request")
        verbose_name_plural = _("Requests")
