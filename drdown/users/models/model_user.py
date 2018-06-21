from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from ..utils.validators import validate_phone


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    photo = models.ImageField(
        upload_to='media/',
        help_text=_("Photo of user."),
        verbose_name=_('Photo'),
        blank=True,
        null=True,
        max_length=500
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
            (("Male"), _("Male")),
            (("Female"), _("Female")),
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

    def age(self):
        today = timezone.datetime.today()
        age = today.year - self.birthday.year - \
            ((today.month,
              today.day) < (self.birthday.month,
                            self.birthday.day))

        if age <= 0:
            diff_month = (today.year - self.birthday.year) * 12 + \
             today.month - self.birthday.month
            age = 0 if diff_month < 6 else 0.5

        return age

    def count_user_specialization(self):

        count = 0

        atributes_to_check = [
            'patient',
            'employee',
            'responsible',
            'healthteam'
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

        if isinstance(self.birthday, timezone.datetime):
            self.birthday = self.birthday.date()

        if self.birthday:
            if timezone.localdate().isoformat() < str(self.birthday):
                raise ValidationError(
                    {'birthday': _("The birthday cannot be in the future!")}
                )
            elif (
                timezone.datetime.strptime(str(self.birthday), "%Y-%m-%d") <
                timezone.datetime.strptime("1900-01-01", "%Y-%m-%d")
            ):
                raise ValidationError(
                    {'birthday': _("This birthday is too old.")}
                )

        return data

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class BaseUserDelete():

    def delete(self, *args, **kwargs):
        self.user.has_specialization = False
        self.user.save()
        User.remove_staff(self.user)
        super().delete(*args, **kwargs)


class BaseUserSave():

    def save(self, *args, **kwargs):
        self.user.clean()
        self.user.save()
        self.clean()  # enforce model validation
        super().save(*args, **kwargs)