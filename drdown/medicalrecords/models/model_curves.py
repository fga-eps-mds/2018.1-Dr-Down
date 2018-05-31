from django.db import models
from django.utils.translation import ugettext_lazy as _
from ...users.models.model_patient import Patient


class Curves(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )
    weight = models.FloatField(
        default=0
    )
    height = models.IntegerField(
        default=0
    )
    cephalic_perimeter = models.FloatField(
        default=0
    )
    bmi = models.FloatField(
        default=0
    )
    age = models.IntegerField(
        default=0
    )

    def get_bmi(self):
        return self.weight / (self.height * self.height)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.bmi = self.get_bmi()
        super(Curves, self).save(force_insert, force_update, *args, **kwargs)
