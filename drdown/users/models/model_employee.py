from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver


from drdown.utils.validators import validate_cpf
from .model_user import User


class Employee(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to=Q(has_specialization=False)
    )

    cpf = models.CharField(
        help_text=_("Please, enter a valid CPF" +
                    " in the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14
    )

    # this is separated from the list because of Django standars
    # if we leave like this we can access the choices from outside
    # example: employee.SPEECH_THERAPHY
    # note: those texts aren't using _() because they are not meant
    # to be translated norshown to the user
    SPEECH_THERAPHY = "SP_TH"
    OCCUPATIONAL_THERAPY = "OC_TH"
    CARDIOLOGY = "CARD"
    NEUROLOGY = "NEURO"
    PEDIATRICS = "PED"
    PSYCHOLOGY = "PSY"
    PHYSIOTHERAPY = "PHYS"
    NURSERY = "NUR"
    SECRETAY = "SEC"
    ADMINISTRATION = "ADM"
    OTHER = "OTH"

    DEPARTAMENT_CHOICES = (
        (SPEECH_THERAPHY, _('Speech Therapy')),
        (OCCUPATIONAL_THERAPY, _('Occupational Therapy')),
        (CARDIOLOGY, _('Cardiology')),
        (NEUROLOGY, _('Neurology')),
        (PEDIATRICS, _('Pediatrics')),
        (PSYCHOLOGY, _('Psychology')),
        (PHYSIOTHERAPY, _('Physiotherapy')),
        (SECRETAY, _('Secretary')),
        (ADMINISTRATION, _('Administration')),
        (NURSERY, _('Nursery')),
        (OTHER, _('Other')),
    )

    departament = models.CharField(
        null=False,
        choices=DEPARTAMENT_CHOICES,
        help_text=_("The departament where this user works."),
        max_length=30
    )

    # const representig the name of the group wich this model
    # will add to the related user
    GROUP_NAME = "Employees"

    def __str__(self):
        return (self.user.get_username() +
                " - " +
                self.get_departament_display())

    def clean(self, *args, **kwargs):

        try:
            user_db = Employee.objects.get(id=self.id).user

            if self.user != user_db:
                raise ValidationError(
                    _("Don't change users"))
            else:
                pass
        except Employee.DoesNotExist:
            pass

        self.user.clean()

    def save(self, *args, **kwargs):

        # we wan't to add the required permissions to the
        # related user, before saving
        self.user.is_staff = True

        try:
            employee_group = Group.objects.get(name=Employee.GROUP_NAME)
        except Group.DoesNotExist:
            employee_group = Group.objects.create(name=Employee.GROUP_NAME)

        # TODO: add permissions to edit Patient and Parent when they get ready
        self.user.groups.add(employee_group)

        self.user.save()

        self.clean()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        # we want to remove staff from a user if he is no longer a employee
        self.user.is_staff = False
        self.user.save()

        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')


@receiver(post_delete, sender=Employee)
def remove_specialization(sender, instance, *args, **kwargs):
    if instance.user.has_specialization:
        instance.user.has_specialization = False
