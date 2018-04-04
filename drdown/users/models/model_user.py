from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    """
    photo = models.ImageField(
        upload_to='users',
        help_text=("Photo of user."),
        verbose_name=('Photo'),
        blank=True,
        null=True
    )
	"""
    name = models.CharField(
        ('Name of User'),
        blank=True,
        max_length=255,
        help_text="Full user name"
    )

    gender = models.CharField(
        ('Gender'),
        choices=(
            ("M", "Male"),
            ("F", "Female"),
        ),
        blank=True,
        max_length=6,
        null=True
    )

    telephone = models.DecimalField(
        ('Telephone'),
        blank=True, null=True,
        decimal_places=0,
        max_digits=12
    )

    birthday = models.DateField(
        ('Birthday'),
        blank=True,
        null=True
    )
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
