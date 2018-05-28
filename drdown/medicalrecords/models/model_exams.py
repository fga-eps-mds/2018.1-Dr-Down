from django.db import models
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError


class Exam(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    file = models.FileField(
        upload_to='media/medicalrecords/exams',
        verbose_name=_('Exam'),
        help_text=_('Exam file'),
    )

    day = models.DateTimeField(
        _('Exam day'),
        help_text=_('Day the exam was performed'),
    )

    CATEGORIES = (
        (None, _("Select a category...")),
        (0, _("Others")),
        (1, _('Structured Physical Exam')),
        (2, _('Vision Exam')),
        (3, _('Ear Exam')),
        (4, _('Hearth Exam')),
        (5, _('Muscle skeletal system Exam')),
        (6, _('Nervous system Exam')),
        (7, _('Blood Exam')),
        (8, _('Bone Densitometry')),
        (9, _('Biopsy')),
        (10, _('Endoscopy')),
        (11, _('Echocardiogram')),
        (12, _('Map and Holter')),
        (13, _('Bioimpedance')),
        (14, _('Neurological examinations')),
        (15, _('Urine Analysis')),
        (16, _('Stool Examination')),
    )

    category = models.IntegerField(
        _('Category'),
        choices=CATEGORIES,
        help_text=_("Please, insert the category of the exam"),
        null=True,
        blank=False,
    )

    observations = models.CharField(
        _('Observations'),
        max_length=200,
        blank=True,
        default=""
    )

    def __str__(self):
        return (
            self.patient.user.get_username() +
            " - " + self.get_category_display()
        )

    def clean(self, *args, **kwargs):
        if self.day:
            if timezone.now() < self.day:
                raise ValidationError(
                    {'day':
                        _("The exam cannot be in the future!")}
                )

        return super(Exam, self).clean()

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")
