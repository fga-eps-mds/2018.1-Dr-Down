from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class SpecificExam(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    structured_physical_exam = models.FileField(
        upload_to='media/medicalrecords/specificexams',
        blank=True,
        verbose_name=_('Structured Physical Exam')
    )

    vision = models.FileField(
        upload_to='media/medicalrecords/specificexams',
        blank=True,
        verbose_name=_('Vision Exam')
    )

    ear = models.FileField(
        upload_to='media/medicalrecords/specificexams',
        blank=True,
        verbose_name=_('Ear Exam')
    )

    hearth = models.FileField(
        upload_to='media/medicalrecords/specificexams',
        blank=True,
        verbose_name=_('Hearth Exam')
    )

    muscle_skeletal_system = models.FileField(
        upload_to='media/medicalrecords/specificexams',
        blank=True,
        verbose_name=_('Muscle skeletal system Exam')
    )

    nervous_system = models.FileField(
        upload_to='media/medicalrecords/specificexams',
        blank=True,
        verbose_name=_('Nervous system Exam')
    )

    author = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
    )

    class Meta:
        verbose_name = _("Specific Exam")
        verbose_name_plural = _("Specific Exams")
