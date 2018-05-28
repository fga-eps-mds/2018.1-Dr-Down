from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from ...users.models.model_patient import Patient
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps


class Curves(models.Model):

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

class Weight(models.Model):

    curves = models.ForeignKey(
        Curves,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    weight = models.FloatField()
    age = models.IntegerField()

    class Meta:
        unique_together = ('curves', 'age',)


class Height(models.Model):

    curves = models.ForeignKey(
        Curves,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    height = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        unique_together = ('curves', 'age',)


class BMI(models.Model):

    curves = models.ForeignKey(
        Curves,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    bmi = models.FloatField()
    age = models.IntegerField()

    @staticmethod
    def calculate_bmi(weight, height):
        return weight / ((height/100)**2)

    class Meta:
        unique_together = ('curves', 'age',)
        verbose_name = _("BMI")
