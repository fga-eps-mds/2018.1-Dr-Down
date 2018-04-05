from django.db import models
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_cpf

from .model_user import User
from .model_patient import Patient


class Responsible(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    cpf = models.CharField(
        help_text=_("Please, use enter a valid CPF in the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14
    )

    def __str__(self):
        return self.user.get_username()
