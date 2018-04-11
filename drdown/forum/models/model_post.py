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
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        _('Create at'),
        help_text=_('The date of create'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Update at'),
        help_text=_('The date of update'),
        null=True)
    created_by = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, null=True,
        related_name='+',
        on_delete=models.CASCADE)
    slug = models.SlugField(
        _('Shortcut'),
        help_text=_('URL string shortcut'),
        max_length=40)

    def __str__(self):
        return self.title


