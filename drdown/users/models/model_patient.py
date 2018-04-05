from django.db import models
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_ses

from .model_user import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ses = models.CharField(
        help_text=_("Please, enter the valid SES number"),
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
        choices=PRIORITIES,
        help_text=_("Please, insert the degree of priority of the patient"),
        )
    mother_name = models.CharField(
                help_text=_("Please, insert your mother name"),
                max_length=80,
    )
    father_name = models.CharField(
                help_text=_("Please, insert your father name"),
                max_length=80,
    )
    COLOR = (
        (5, _('White')),
        (4, _('Black')),
        (3, _('Yellow')),
        (2, _('Brown')),
        (1, _('Indigenous')),
    )
    ethnicity = models.IntegerField(
        choices=COLOR,
        help_text=_("Please insert the ethnicity of the patient"),
    )
    sus_number = models.CharField(
        help_text=_("Please, enter the valid SUS number"),
        unique=True,
        default='',
        max_length=11,
    )
    civil_registry_of_birth = models.CharField(
        help_text=_("Please, enter the civil registry of birth number"),
        unique=True,
        default='',
        max_length=11,
    )
    declaration_of_live_birth = models.CharField(
        help_text=_("Please, enter the declaration of live birth number"),
        unique=True,
        default='',
        max_length=11,
    )

    def __str__(self):
        return self.user.get_username()
