from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from ..utils.validators import validate_cpf
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .model_user import User, BaseUserSave, BaseUserDelete


class Responsible(BaseUserSave, BaseUserDelete, models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to=Q(has_specialization=False),
        verbose_name=_('User')
    )

    cpf = models.CharField(
        help_text=_("Please, use enter a valid CPF in" +
                    "the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14,
    )

    def have_patient_needing_atention(self):

        response = False
        patients = self.patient_set.all()

        for patient in patients:
            if patient.have_procedures_almost_late():
                response = True
                break

        return response

    def clean(self, *args, **kwargs):

        try:
            user_db = Responsible.objects.get(id=self.id).user

            if self.user != user_db:
                raise ValidationError(
                    _("Don't change users"))
            else:
                pass
        except Responsible.DoesNotExist:
            pass

        self.user.clean()

    def __str__(self):
        return self.user.get_username()

    class Meta:
        verbose_name = _('Responsible')
        verbose_name_plural = _('Responsibles')
