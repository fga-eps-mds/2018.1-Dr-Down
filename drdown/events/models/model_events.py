from django.db import models
from django.utils.translation import ugettext_lazy as _


class Events(models.Model):

    name = models.CharField(
        _('Name'),
        help_text = _('Name of event'),
        max_length= 50,
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
    description =  models.TextField(
        _('Description'),
        help_text=_('Description from event'),
        max_length=500,
        blank=True,
    )

    organize_by = models.CharField(
        _('Organize by'),
        max_length = 80,
        help_text=_('Person who organize the event'),
    )

    value = models.DecimalField(
        _('Value of event'),
        help_text=_('Event value if that is paid'),
        decimal_places = 2,
        max_digits = 4,
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
