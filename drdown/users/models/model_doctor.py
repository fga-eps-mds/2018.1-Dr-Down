from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from drdown.utils.validators import validate_cpf
from .model_user import User
from drdown.utils.validators import validate_crm


class Doctor(models.Model):

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

    crm = models.CharField(
        validators=[validate_crm],
        max_length=7,
        help_text=_("Use enter a valid CRM. \n" +
                    "Enter 7 digits from 0 to 9"
                    )

    )

    SPEECH_THERAPHY = _("Speech Therapy")
    OCCUPATIONAL_THERAPY = _("Occupational Therapy")
    CARDIOLOGY = _("Cardiology")
    NEUROLOGY = _("Neurology")
    PEDIATRICS = _("Pediatrics")
    PSYCHOLOGY = _("Psychology")
    PHYSIOTHERAPY = _("Physiotherapy")

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
        _('Speciality'),
        choices=SPECIALITY_CHOICES,
        help_text=_("The speciality that this doctor works."),
        max_length=30,
        blank=True
    )

    # const representig the name of the group wich this model will add to the
    # related user
    GROUP_NAME = "Doctors"

    def clean(self, *args, **kwargs):

        try:
            user_db = Doctor.objects.get(id=self.id).user

            if self.user != user_db:
                raise ValidationError(
                    _("Don't change users"))
            else:
                pass
        except Doctor.DoesNotExist:
            pass

        self.user.clean()

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
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')

