from django.db import models
from django.utils.translation import ugettext_lazy as _


class Events(models.Model):

    name = models.CharField(
        _('Name'),
        help_text=_('Name of event'),
        max_length=50,
        default=""
    )
    location = models.CharField(
        _('Location'),
        help_text=_('Location of event'),
        max_length=50,
        default=""
    )
    date = models.DateField(
        _('Date'),
        help_text=_('Date of event'),
        max_length=50
    )
    time = models.TimeField(
        _('Time'),
        help_text=_('Time of event'),
        max_length=50
    )
    description = models.TextField(
        _('Description'),
        help_text=_('Description from event'),
        max_length=500,
        blank=True,
    )

    organize_by = models.CharField(
        _('Organize by'),
        max_length=80,
        help_text=_('Person who organize the event'),
    )

    free = models.BooleanField(default=False)

    value = models.FloatField(
        _('Value of event'),
        help_text=_('Event value if that is paid'),
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def clean_status(self):
        # when field is cleaned, we always return the existing model field.
        return self.instance.status
