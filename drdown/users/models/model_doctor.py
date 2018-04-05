from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group

from drdown.utils.validators import validate_cpf
from .model_user import User


class Doctor(models.Model):

	SPEECH_THERAPHY = "SP_TH"
    OCCUPATIONAL_THERAPY = "OC_TH"
    CARDIOLOGY = "CARD"
    NEUROLOGY = "NEURO"
    PEDIATRICS = "PED"
    PSYCHOLOGY = "PSY"
    PHYSIOTHERAPY = "PHYS"

    SPECIALITY_CHOICES = (
        (SPEECH_THERAPHY, _('Speech Therapy')),
        (OCCUPATIONAL_THERAPY, _('Occupational Therapy')),
        (CARDIOLOGY, _('Cardiology')),
        (NEUROLOGY, _('Neurology')),
        (PEDIATRICS, _('Pediatrics')),
        (PSYCHOLOGY, _('Psychology')),
        (PHYSIOTHERAPY, _('Physiotherapy')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    cpf = models.CharField(
    	choices=SPECIALITY_CHOICES,
        help_text=_(
            "Please, use enter a valid CPF in the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14
    )

    crm = models.IntegerField(
        max_length=30,
        blank=True
    )
    speciality = models.CharField(
        help_text=_("The speciality that this doctor works."),
        max_length=30,
        blank=True
    )


def __str__(self):
    return self.user.get_username() + " - " + self.get_departament_display()


class Meta:
    verbose_name = _('Doctor')
    verbose_name_plural = _('Doctors')
