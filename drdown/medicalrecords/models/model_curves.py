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


@receiver(post_save, sender=Height)
@receiver(post_save, sender=Weight)
def create_BMI(sender, instance, **kwargs):


    height_object = apps.get_model('medicalrecords', 'Height') \
            .objects.filter(
                curves=instance.curves,
                age=instance.age
            ).first()

    weight_object = apps.get_model('medicalrecords', 'Weight') \
            .objects.filter(
                curves=instance.curves,
                age=instance.age
            ).first()

    bmi_object =  apps.get_model('medicalrecords', 'BMI') \
            .objects.filter(
                curves=instance.curves,
                age=instance.age
            ).first()

    if bmi_object:
        # if a bmi exists for an age weight and height exists, and it should be
        # updated with the new calculated value
        bmi_object.bmi = BMI.calculate_bmi(weight_object.weight, height_object.height)
        bmi_object.save()

    elif height_object and weight_object:
        apps.get_model('medicalrecords', 'BMI') \
            .objects.create(
                curves=instance.curves,
                age=instance.age,
                bmi=BMI.calculate_bmi(
                    weight_object.weight,
                    height_object.height
                )
            )