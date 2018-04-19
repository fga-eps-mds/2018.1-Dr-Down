from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_phone
import datetime


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    photo = models.ImageField(
        upload_to='media/',
        help_text=_("Photo of user."),
        verbose_name=_('Photo'),
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
            ("Male", "Male"),
            ("Female", "Female"),
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

    has_specialization = models.BooleanField(
        default=False,
        editable=False
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_short_name(self):
        return(self.first_name)

    def count_user_specialization(self):

        count = 0

        atributes_to_check = [
            'patient',
            'employee',
            'responsible',
            'health_team'
        ]

        for attr in atributes_to_check:
            if hasattr(self, attr):
                count += 1

        return count

    def remove_staff(user):

        # we want to remove staff from a user if he is no longer has a
        # specialization that needs it
        user.is_staff = False
        user.save()

    def clean(self, *args, **kwargs):
        data = super(User, self).clean()

        if self.count_user_specialization() > 1:
            error = ValidationError(
               {'user': _("This user is already specialized!")}
            )

            raise error
        else:
            self.has_specialization = (self.count_user_specialization() is 1)

        return data

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
