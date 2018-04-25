from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from drdown.careline.models.model_procedure import Procedure

from drdown.users.models import Patient


class Checklist(models.Model):

    CARE_LINE = [
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Nutritional and growind/development"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                Procedure.AGES,
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Early stimulation"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                    Procedure.AGE_SIX_MONTHS,
                    Procedure.AGE_ONE_YEAR,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                ],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Psychosocial support to the" +
                  "family (associations, references)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                Procedure.AGES,
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Physiotherapy"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                    Procedure.AGE_SIX_MONTHS,
                    Procedure.AGE_ONE_YEAR,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Speech Therapy"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                Procedure.AGES,
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Cardiologic (echocardiogram, electrocardiogram)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [
                    Procedure.AGE_ONE_YEAR,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Genetics (karyotype, counseling)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Audiological (otoacoustic emissions, PEATE)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Audiological (audio/impedanciometry, PEATE) +" +
                  "otolaryngologist"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_SIX_MONTHS,
                    Procedure.AGE_ONE_YEAR,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Dentistry"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_SIX_MONTHS,
                    Procedure.AGE_ONE_YEAR,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [
                    Procedure.AGE_NEWBORN,
                ],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Ophthalmologic"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                    Procedure.AGE_ONE_YEAR,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Other therapies (occupational therapy, swimming," +
                  "psychomotricity, psychopedagogy, hydro/equo/music" +
                  "therapy, arts, others)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_SIX_MONTHS,
                    Procedure.AGE_ONE_YEAR,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Abdominal ultrasound"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [
                    Procedure.AGE_THREE_YEARS,
                ],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Atlantoaxial X-ray * (extension, flexion and neutral)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Laboratory tests ** (blood count, thyrogram," +
                  "blood glucose and lipidogram - if diabetes/obesity" +
                  "is suspected)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                    Procedure.AGE_ONE_YEAR,
                    Procedure.AGE_TWO_YEARS,
                    Procedure.AGE_THREE_YEARS,
                    Procedure.AGE_FIVE_YEARS,
                    Procedure.AGE_SIX_TO_TEN_YEARS,
                ],
            Procedure.PROCEDURE_AGES_WHEN_NEEDED:
                [],
        },
        {
            Procedure.PROCEDURE_DESCRIPTION:
                _("Research for Celiac Disease (antigliadin antibody)"),
            Procedure.PROCEDURE_AGES_REQUIRED:
                [
                    Procedure.AGE_NEWBORN,
                    Procedure.AGE_TWO_YEARS,
                ],
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
    instance.save()  # only called once, so there is no recursion error
