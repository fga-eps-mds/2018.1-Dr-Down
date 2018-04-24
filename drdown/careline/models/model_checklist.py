from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from drdown.careline.models.model_procedure import Procedure

from drdown.users.models import Patient


class Checklist(models.Model):

    # procedure identifiers for dictionary
    PROCEDURE_NUTRITION = 'nut'

    CARE_LINE = [
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Nutritional and growind/development"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                Procedure.AGES,
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
    ]

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
    )

    initialized = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        editable=False
    )


@receiver(post_save, sender=Checklist)
def create_procedures(sender, instance, **kwargs):

    if instance.initialized:
        return

    for procedure in Checklist.CARE_LINE:
        p = Procedure.objects.create(
            careline=instance,
            description=procedure[Procedure.PROCEDURE_DESCRIPTION],
        )

        p.create_check_items(
            ages_required=procedure[Procedure.PROCEDURE_AGES_REQUIRED],
            ages_needed=procedure[Procedure.PROCEDURE_AGES_WHEN_NEEDED]
        )

    instance.initialized = True
    instance.save() # only called once, so there is no recursion error
