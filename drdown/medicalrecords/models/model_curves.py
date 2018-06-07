from django.db import models
from django.utils.translation import ugettext_lazy as _
from ...users.models.model_patient import Patient
from django.core.validators import MinValueValidator


class Curves(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )
    weight = models.FloatField(
        verbose_name=_('Weight'),
        help_text=_('Weight in kg'),
    )
    height = models.IntegerField(
        verbose_name=_('Height'),
        help_text=_('Height in cm'),
        validators=[MinValueValidator(0.1)],
    )
    cephalic_perimeter = models.FloatField(
        verbose_name=_('Cephalic Perimeter'),
        help_text=_('Perimeter in cm')
    )
    bmi = models.FloatField(
        verbose_name=_('BMI'),
        default=0.0
    )
    age = models.IntegerField(
        verbose_name=_('Age'),
        help_text=_('Age in months')
    )

    def get_bmi(self):
        return self.weight / (self.height/100 * self.height/100)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.bmi = self.get_bmi()
        if self.age >= 24:
            self.cephalic_perimeter = 0

        super(Curves, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        unique_together = ("patient", "age")
