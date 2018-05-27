from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from ...users.models.model_patient import Patient


class Curves(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Patient')
    )

    __original_weight = None

    def __init__(self, *args, **kwargs):
        super(Curves, self).__init__(*args, **kwargs)
        self.__original_weight = self.weight

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.weight != self.__original_weight:
            # weight changed
            new_weight = WeightHistory(patient=self.patient, weight=self.weight)
            new_weight.save()
        super(Curves, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_weight = self.weight

    def weight_history(self):
        return WeightHistory.objects.filter(patient=self.patient).order_by('-age')


class WeightHistory(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Patient')
    )
    weight = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        unique_together = ('patient', 'age',)

    def save(self, *args, **kwargs):
        # get age in years
        born = self.patient.user.birthday
        today = timezone.today()
        age_years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        # convert to months
        self.age = age_years * 12
        super(WeightHistory, self).save(*args, **kwargs)
