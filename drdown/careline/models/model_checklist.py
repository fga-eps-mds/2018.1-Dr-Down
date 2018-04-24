from django.db import models
from django.utils.translation import ugettext_lazy as _

from drdown.careline.models.model_procedure import Procedure

from drdown.users.models import Patient


class Checklist(models.Model):

    # procedure identifiers for dictionary
    PROCEDURE_NUTRITION = 'nut'

    CARE_LINE = {
        PROCEDURE_NUTRITION: {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Nutritional and growind/development"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                Procedure.AGES,
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
    }

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

    def save(self, *args, **kwargs):

        if not self.initialized:
            self.create_procedures()
            self.initialized = True

        super().save(*args, **kwargs)

    def create_procedures(self):

        if self.initialized:
            return

        for procedure in Checklist.CARE_LINE:
            p = Procedure.objects.create(
                careline=self,
                description=procedure[Procedure.PROCEDURE_DESCRIPTION],
            )

            p.create_checkitens(
                ages_required=procedure[Procedure.PROCEDURE_AGES_REQUIRED],
                ages_needed=procedure[Procedure.PROCEDURE_AGES_WHEN_NEEDED]
            )
