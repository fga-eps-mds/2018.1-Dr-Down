from django.db import models
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_ses

from .model_user import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    ses = models.CharField(
        help_text=_("Please, enter the valid SES"),
        unique=True,
        max_length=9,
        validators=[validate_ses],
    )
    PRIORITIES = (
        (5, _('Not urgent')),
        (4, _('Not very urgent')),
        (3, _('Urgent')),
        (2, _('Very urgent')),
        (1, _('Emerging')),
      )
    priority = models.IntegerField(
        default=5, choices=PRIORITIES,
        help_text=_("Please, insert the degree of priority of the patient"),
        )

    def __str__(self):
        return self.user.get_username()
