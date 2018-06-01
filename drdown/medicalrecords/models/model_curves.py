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
        default=0.0,
        help_text=_('Weight in kg')
    )
    height = models.IntegerField(
        default=0,
        help_text=_('Height in cm'),
    )
    cephalic_perimeter = models.FloatField(
        default=0.0,
        help_text=_('Perimeter in cm')
    )
    bmi = models.FloatField(
        default=0.0
    )
    age = models.IntegerField(
        default=0,
        help_text=_('Age in months')
    )

    def get_bmi(self):
        return self.weight / (self.height * self.height)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.bmi = self.get_bmi()
        super(Curves, self).save(force_insert, force_update, *args, **kwargs)
