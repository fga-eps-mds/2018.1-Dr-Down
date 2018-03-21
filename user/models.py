from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=50, default=None)
    password = models.CharField(max_length=50, default=None)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField(auto_now=False,
                                auto_now_add=False, default=None)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default=None)
    telephone = models.DecimalField(max_digits=12,
                                    decimal_places=0, default=None)

    def __str__(self):
        return self.email
