from django.db import models
from drdown.users.models.model_user import User
from .model_post import Post
from django.utils.translation import ugettext_lazy as _


class Commentary(models.Model):
    message = models.TextField(
        _('Message'),
        max_length=4000
    )
    post = models.ForeignKey(
        Post,
        related_name='commentaries',
        on_delete=models.CASCADE,
        verbose_name=_("Post")
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
        related_name='commentaries',
        on_delete=models.CASCADE,
        verbose_name=_("Created by")
    )

    class Meta:
        verbose_name = _("Commentary")
        verbose_name_plural = _("Commentaries")
