from django.db import models
from drdown.users.models import User
from .model_category import Category
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(
        _('Title'),
        help_text=_('Title of post'),
        max_length=50
    )
    message = models.TextField(
        _('Message'),
        help_text=_('Message of post'),
        max_length=4000
    )
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name=_("Category")
    )
    created_at = models.DateTimeField(
        _('Created at'),
        help_text=_('Date of creation'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        help_text=_('Date of update'),
        null=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name=_("Created by")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
