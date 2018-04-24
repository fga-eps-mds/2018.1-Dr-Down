from django.db import models
from django.utils.translation import ugettext_lazy as _

from drdown.careline.models import CheckItem


class Procedure(models.Model):

    careline = models.ForeignKey('careline.Checklist', on_delete=models.CASCADE)

    # consts for unifying procedure parameters
    PROCEDURE_DESCRIPTION = 'description'
    PROCEDURE_AGES_REQUIRED = 'ages_required'
    PROCEDURE_AGES_WHEN_NEEDED = 'ages_needed'

    AGE_NEWBORN = 'NB'
    AGE_SIX_MONTHS = '6M'
    AGE_ONE_YEAR = '1Y'
    AGE_TWO_YEARS = '2Y'
    AGE_THREE_YEARS = '3Y'
    AGE_FIVE_YEARS = '5Y'
    AGE_SIX_TO_TEN_YEARS = '6_10Y'

    AGES = [
        AGE_NEWBORN,
        AGE_SIX_MONTHS,
        AGE_ONE_YEAR,
        AGE_TWO_YEARS,
        AGE_THREE_YEARS,
        AGE_FIVE_YEARS,
        AGE_SIX_TO_TEN_YEARS,
    ]

    description = models.TextField(blank=False, null=False)

    initialized = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        editable=False
    )

    def convert_age_to_item(age):
        pass

    def create_chekitens(self, ages_required, ages_needed):

        if self.initialized:
            return

        for age in Procedure.AGES:
            CheckItem.objects.create(
                procedure=this,
                age=age,
                required=(age in ages_required),
                when_needed=(age in ages_needed),
                check=False
            )

        self.initialized = True
        self.save()
