from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        _('Name'),
        help_text=_('Name of category'),
        max_length=30,
        unique=True
    )
    description = models.CharField(
        _('Description'),
        help_text=_('Description'),
        max_length=100
    )
    slug = models.SlugField(
        _('Shortcut'),
        help_text=_('URL string shortcut'),
        max_length=40
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
