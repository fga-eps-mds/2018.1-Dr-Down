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


class Graphic(models.Model):

    title = models.CharField(
        max_length=100,
    )

    HEIGHT = "Height"
    WEIGHT = "Weight"
    PERIMETER = "Perimeter"
    BMI = "BMI"

    TYPE_CHOICES = (
        (HEIGHT,  _("Height")),
        (WEIGHT, _("Weight")),
        (PERIMETER, _("Perimeter")),
        (BMI, _("BMI")),
    )

    type = models.CharField(
        choices=TYPE_CHOICES,
        default=HEIGHT,
        max_length=15,
    )

    GENDER_CHOICES = (
        ("M", _("Male")),
        ("F", _("Female"))
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        default="M",
        max_length=10,
    )

    INTERVAL_CHOICES = (
        ("months", _("0-35 months")),
        ("years", _("3-20 years")),
    )

    interval = models.CharField(
        choices=INTERVAL_CHOICES,
        default="months",
        max_length=20,
    )


class YAxis(models.Model):

    graphic = models.ForeignKey(
        Graphic,
        on_delete=models.CASCADE,
        related_name="YAxis"
    )


class Point(models.Model):

    y_axis = models.ForeignKey(
        YAxis,
        on_delete=models.CASCADE,
        related_name="Point"
    )

    value = models.FloatField(
        default=0.0,
    )


class Header(models.Model):

    y_axis = models.ForeignKey(
        YAxis,
        on_delete=models.CASCADE,
        related_name="Header"
    )

    value = models.CharField(
        max_length=10,
    )
