from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from ..utils.validators import validate_cpf
from .model_user import User
from ..utils.validators import validate_register_number


class HealthTeam(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to=Q(has_specialization=False),
        verbose_name=_('User')
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
    CREFITO = ("CREFITO")
    COREN = ("COREN")
    CREFONO = ("CREFONO")

    ACRONYM_CHOICES = (
        (CRM, 'CRM'),
        (CRP, 'CRP'),
        (CREFITO, ('CREFITO')),
        (COREN, ('COREN')),
        (CREFONO, ('CREFONO')),
    )

    council_acronym = models.CharField(
        _('Council Acronym'),
        choices=ACRONYM_CHOICES,
        help_text=_("The Regional Council."),
        max_length=30
    )

    register_number = models.CharField(
        _('Register Number'),
        validators=[validate_register_number],
        max_length=9,
        help_text=_("Enter a valid register number.")

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

    SPEECH_THERAPHY = "Speech Therapy"
    PSYCHOLOGY = "Psychology"
    PHYSIOTHERAPY = "Physiotherapy"
    OCCUPATIONAL_THERAPY = "Occupational Therapy"
    GENERAL_PRACTITIONER = "General Practitioner"
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    PEDIATRICS = "Pediatrics"
    NURSING = "Nursing"

    SPECIALITY_CHOICES = (
        (SPEECH_THERAPHY, _('Speech Therapy')),
        (PSYCHOLOGY, _('Psychology')),
        (PHYSIOTHERAPY, _('Physiotherapy')),
        (OCCUPATIONAL_THERAPY, _('Occupational Therapy')),
        (GENERAL_PRACTITIONER, _('General Practitioner')),
        (CARDIOLOGY, _('Cardiology')),
        (NEUROLOGY, _('Neurology')),
        (PEDIATRICS, _('Pediatrics')),
        (NURSING, _('Nursing')),
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

    def get_speciality_relation_list(self):

        crm = [
            HealthTeam.GENERAL_PRACTITIONER,
            HealthTeam.CARDIOLOGY,
            HealthTeam.NEUROLOGY,
            HealthTeam.PEDIATRICS,
        ]

        crp = [
            HealthTeam.PSYCHOLOGY,
        ]

        crefito = [
            HealthTeam.OCCUPATIONAL_THERAPY,
            HealthTeam.PHYSIOTHERAPY,
        ]

        coren = [
            HealthTeam.NURSING,
        ]

        crefono = [
            HealthTeam.SPEECH_THERAPHY,
        ]

        return{
            HealthTeam.CRM: crm,
            HealthTeam.CRP: crp,
            HealthTeam.CREFITO: crefito,
            HealthTeam.CREFONO: crefono,
            HealthTeam.COREN: coren,
        }[self.council_acronym]

    def clean(self, *args, **kwargs):

        try:
            user_db = HealthTeam.objects.get(id=self.id).user

            if self.user != user_db:
                raise ValidationError(
                    _("Don't change users"))
            else:
                pass
        except HealthTeam.DoesNotExist:
            pass

        relational_list = self.get_speciality_relation_list()

        if self.speciality not in relational_list:

            raise ValidationError(
                _("The %(register)s doesn't inscribe professionals" +
                  "with %(speciality)s graduation, please correct"),
                params={
                    'speciality': self.get_speciality_display(),
                    'register': self.get_council_acronym_display()
                }
            )

        self.user.clean()

    def save(self, *args, **kwargs):

        # we wan't to add the required permissions to the related user, before
        # saving
        self.user.is_staff = True

        try:
            health_team_group = Group.objects.get(name=HealthTeam.GROUP_NAME)
        except Group.DoesNotExist:
            health_team_group = Group.objects.create(
               name=HealthTeam.GROUP_NAME
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
