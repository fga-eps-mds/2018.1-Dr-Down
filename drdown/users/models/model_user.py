from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_phone
import datetime


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    photo = models.ImageField(
        upload_to='media/',
        help_text="Photo of user.",
        verbose_name='Photo',
        blank=True,
        null=True
    )

    name = models.CharField(
        _('Name'),
        blank=False,
        max_length=255,
        help_text=_("Full user name")

    )

    gender = models.CharField(
        _('Gender'),
        choices=(
            ("M", "Male"),
            ("F", "Female"),
        ),
        blank=False,
        max_length=6,
        null=True
    )

    telephone = models.CharField(
        _('Telephone'),
        blank=False,
        null=True,
        max_length=14,
        validators=[validate_phone],
        help_text=_("(xx)xxxxx-xxxx or (xx)xxxx-xxxx"),

    )

    birthday = models.DateField(
        _('Birthday'),
        help_text=_("xx/xx/xxxx"),
        blank=False,
        null=True
    )

    created_at = models.DateField(
      _('Created at'),
      blank=False,
      null=True
    )

    updated_at = models.DateField(
       _('Updated at'),
       blank=False,
       null=True
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_short_name(self):
        return(self.first_name)
