from django.db import models
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class Exam(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_('Patient')
    )

    file = models.FileField(
        upload_to='media/medicalrecords/exams',
        verbose_name=_('Exam')
    )

    day = models.DateTimeField(
        _('Exam day'),
        help_text=_('Day the exam was performed'),
    )

    STATUS = (
        (3, _('Executed')),
        (2, _('Collected')),
        (1, _('Marked examination')),
    )

    status = models.IntegerField(
        _('Status'),
        choices=STATUS,
        help_text=_("Please, insert the status of the exam"),
    )

    name = models.CharField(
        _('Exam Name'),
        max_length=200
    )

    author = models.ForeignKey(
        HealthTeam,
        on_delete=models.CASCADE,
        verbose_name=_("Author")
    )

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")
