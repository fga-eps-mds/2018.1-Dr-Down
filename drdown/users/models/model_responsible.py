from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_cpf
from django.core.exceptions import ValidationError

from .model_user import User
from .model_patient import Patient


class Responsible(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                limit_choices_to=Q(patient=None))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    cpf = models.CharField(
        help_text=_("Please, use enter a valid CPF in" +
                    "the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14,
    )

    def clean(self, *args, **kwargs):

        if hasattr(self.user, 'patient'):
            raise ValidationError(
                {'user': _("A patient cannot be a responsible!")}
            )

    def save(self, *args, **kwargs):
        self.clean()  # enforce model validation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_username()
