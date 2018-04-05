from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from drdown.utils.validators import validate_phone

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    photo = models.ImageField(
        upload_to='img/',
        help_text=("Photo of user."),
        verbose_name=('Photo'),
        blank=True,
        null=True
    )

    name = models.CharField(
        ('Name of User'),
        blank=False,
        max_length=255,
        help_text="Full user name"

    )

    gender = models.CharField(
        ('Gender'),
        choices=(
            ("M", "Male"),
            ("F", "Female"),
        ),
        blank=False,
        max_length=6,
        null=True
    )

    telephone = models.CharField(
        ('Telephone'),
        blank=False,
        null=True,
        max_length=14,
         validators=[validate_phone],
        help_text=("(xx)xxxxx-xxxx")

    )

    birthday = models.DateField(
        ('Birthday'),
        help_text=("xx/xx/xxxx"),
        blank=False,
        null=True
    )

    created_at = models.DateField(
    	('Created at'),
    	blank=False,
    	null=True
    )

    updated_at = models.DateField(
    	('Updated at'),
    	blank=False,
    	null=True
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_short_name(self):
        return(self.first_name)