from django.db import models
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class Risk(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    PRIORITIES = (
      (5, _('Not urgent')),
      (4, _('Not very urgent')),
      (3, _('Urgent')),
      (2, _('Very urgent')),
      (1, _('Emerging')),
    )
    priority_speech_theraphy = models.IntegerField(
      _('Speech Therapy Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree of" +
                  " speech therapy priority of the patient"),
      default=5,
    )
    priority_psychology = models.IntegerField(
      _('Psychology Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree" +
                  " of psychology priority of the patient"),
      default=5,
    )
    priority_physiotherapy = models.IntegerField(
      _('Physiotherapy Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree" +
                  " of physiotherapy priority of the patient"),
      default=5,
    )
    priority_cardiology = models.IntegerField(
      _('Cardiology Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree" +
                  " of cardiology priority of the patient"),
      default=5,
    )
    priority_neurology = models.IntegerField(
      _('Neurology Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree" +
                  " of neurology priority of the patient"),
      default=5,
    )
    priority_pediatrics = models.IntegerField(
      _('Pediatrics Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree" +
                  " of pediatrics priority of the patient"),
      default=5,
    )
    priority_general_practitioner = models.IntegerField(
      _('General Practitioner Priority'),
      choices=PRIORITIES,
      help_text=_("Please," +
                  " insert the degree" +
                  " of general practitioner priority of the patient"),
      default=5,
    )

    class Meta:
        verbose_name = _('Risk')
        verbose_name_plural = _('Risks')

    def __str__(self):
        return self.patient.user.get_username() + " - " + "Risks"
