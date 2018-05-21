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
    priority = models.IntegerField(
      _('Priority'),
      choices=PRIORITIES,
      help_text=_("Please, insert the degree of priority of the patient"),
    )
