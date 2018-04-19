from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from drdown.utils.validators import validate_cpf
from .model_user import User
from drdown.utils.validators import validate_register_number


class Health_Team(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to=Q(has_specialization=False)
    )

    cpf = models.CharField(
        help_text=_(
            "Please, use enter a valid CPF in the following format:" +
            "XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14
    )

    CRM = ("CRM")
    CRP = ("CRP")
    COFFITO = ("COFFITO")

    ACRONYM_CHOICES = (
        (CRM, 'CRM'),
        (CRP, 'CRP'),
        (COFFITO, _('COFFITO')),
    )

    council_acronym = models.CharField(
        _('Council Acronym'),
        choices=ACRONYM_CHOICES,
        help_text=_("The Regional Council."),
        max_length=30
    )

    register_number = models.CharField(
        validators=[validate_register_number],
        max_length=7,
        help_text=_("Use enter a valid register number. \n" +
                    "Enter 7 digits"
                    )

    )

    AC = ("AC")
    AL = ("AL")
    AP = ("AP")
    BA = ("BA")
    CE = ("CE")
    DF = ("DF")
    ES = ("ES")
    GO = ("GO")
    MA = ("MA")
    MG = ("MG")
    MS = ("MS")
    MT = ("MT")
    PA = ("PA")
    PB = ("PB")
    PE = ("PE")
    PI = ("PI")
    PR = ("PR")
    RJ = ("RJ")
    RN = ("RN")
    RO = ("RO")
    RR = ("RR")
    RS = ("RS")
    SC = ("SC")
    SE = ("SE")
    SP = ("SP")
    TO = ("TO")

    UF_CHOICES = (
        (AC, 'AC'),
        (AL, 'AL'),
        (AP, 'AP'),
        (BA, 'BA'),
        (CE, 'CE'),
        (DF, 'DF'),
        (ES, 'ES'),
        (GO, 'GO'),
        (MA, 'MA'),
        (MG, 'MG'),
        (MS, 'MS'),
        (MT, 'MT'),
        (PA, 'PA'),
        (PB, 'PB'),
        (PE, 'PE'),
        (PI, 'PI'),
        (PR, 'PR'),
        (RJ, 'RJ'),
        (RN, 'RN'),
        (RO, 'RO'),
        (RR, 'RR'),
        (RS, 'RS'),
        (SC, 'SC'),
        (SE, 'SE'),
        (SP, 'SP'),
        (TO, 'TO'),
    )

    registration_state = models.CharField(
        _('State'),
        choices=UF_CHOICES,
        help_text=_("The registration state of member of health team."),
        max_length=30
    )

    SPEECH_THERAPHY = _("Speech Therapy")
    OCCUPATIONAL_THERAPY = _("Occupational Therapy")
    CARDIOLOGY = _("Cardiology")
    NEUROLOGY = _("Neurology")
    PEDIATRICS = _("Pediatrics")
    PSYCHOLOGY = _("Psychology")
    PHYSIOTHERAPY = _("Physiotherapy")
    DOCTOR = _("Doctor")

    SPECIALITY_CHOICES = (
        (SPEECH_THERAPHY, _('Speech Therapy')),
        (OCCUPATIONAL_THERAPY, _('Occupational Therapy')),
        (CARDIOLOGY, _('Cardiology')),
        (NEUROLOGY, _('Neurology')),
        (PEDIATRICS, _('Pediatrics')),
        (PSYCHOLOGY, _('Psychology')),
        (PHYSIOTHERAPY, _('Physiotherapy')),
        (DOCTOR, _('Doctor')),
    )

    speciality = models.CharField(
        _('Speciality'),
        choices=SPECIALITY_CHOICES,
        help_text=_("The speciality that this member of health team works."),
        max_length=30
    )

    # const representig the name of the group wich this model will add to the
    # related user
    GROUP_NAME = "Health_Team"

    def clean(self, *args, **kwargs):

        try:
            user_db = Health_Team.objects.get(id=self.id).user

            if self.user != user_db:
                raise ValidationError(
                    _("Don't change users"))
            else:
                pass
        except Health_Team.DoesNotExist:
            pass

        self.user.clean()

    def save(self, *args, **kwargs):

        # we wan't to add the required permissions to the related user, before
        # saving
        self.user.is_staff = True

        try:
            health_team_group = Group.objects.get(name=Health_Team.GROUP_NAME)
        except Group.DoesNotExist:
            health_team_group = Group.objects.create(
               name=Health_Team.GROUP_NAME
            )

        # TODO: add permissions to edit Patient and Parent when they get ready
        self.user.groups.add(health_team_group)

        self.user.clean()
        self.user.save()

        self.clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_username() + " - " + self.get_speciality_display()

    def delete(self, *args, **kwargs):
        self.user.has_specialization = False
        self.user.save()
        User.remove_staff(self.user)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Health Team')
        verbose_name_plural = _('Health Team')
        unique_together = (
            ("registration_state", "register_number", "council_acronym")
        )
