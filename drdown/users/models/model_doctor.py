from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group

from drdown.utils.validators import validate_cpf
from .model_user import User


class Doctor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    cpf = models.CharField(
        help_text=_(
            "Please, use enter a valid CPF in the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14
    )

    crm = models.CharField(
        max_length=7
    )

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

    speciality = models.CharField(
        choices=SPECIALITY_CHOICES,
        help_text=_("The speciality that this doctor works."),
        max_length=30,
        blank=True
    )

    # const representig the name of the group wich this model will add to the
    # related user
    GROUP_NAME = "Doctors"

    def save(self, *args, **kwargs):

        # we wan't to add the required permissions to the related user, before
        # saving
        self.user.is_staff = True

        try:
            doctor_group = Group.objects.get(name=Doctor.GROUP_NAME)
        except Group.DoesNotExist:
            doctor_group = Group.objects.create(name=Doctor.GROUP_NAME)

        # TODO: add permissions to edit Patient and Parent when they get ready
        self.user.groups.add(doctor_group)

        self.user.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_username() + " - " + self.get_speciality_display()

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')