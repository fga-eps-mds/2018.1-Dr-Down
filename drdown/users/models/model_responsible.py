from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_cpf
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .model_user import User


class Responsible(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to=Q(has_specialization=False)
    )

    cpf = models.CharField(
        help_text=_("Please, use enter a valid CPF in" +
                    "the following format: XXX.XXX.XXX-XX"),
        unique=True,
        validators=[validate_cpf],
        max_length=14,
    )

    def clean(self, *args, **kwargs):
        self.user.clean()

    def save(self, *args, **kwargs):
        self.clean()  # enforce model validation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_username()


@receiver(post_delete, sender=Responsible)
def remove_specialization(sender, instance, *args, **kwargs):
    if instance.user.has_specialization:
        instance.user.has_specialization = False
