from django.db import models
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _

class Risk(models.Model):

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
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_psychology = models.IntegerField(
      _('Psychology Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_physiotherapy = models.IntegerField(
      _('Physiotherapy Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_occupational_therapy = models.IntegerField(
      _('Occupational Therapy Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_cardiology = models.IntegerField(
      _('Cardiology Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_neurology = models.IntegerField(
      _('Neurology Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_pediatrics = models.IntegerField(
      _('Pediatrics Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
    priority_nursing = models.IntegerField(
      _('Nursing Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
