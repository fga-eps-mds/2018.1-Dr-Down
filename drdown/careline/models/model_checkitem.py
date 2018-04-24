from django.db import models
from django.utils.translation import ugettext_lazy as _


class CheckItem(models.Model):

    procedure = models.ForeignKey('careline.Procedure', on_delete=models.CASCADE)

    age = models.IntegerField()

    required = models.BooleanField(blank=False, null=False, default=False)
    when_needed = models.BooleanField(blank=False, null=False, default=False)

    check = models.BooleanField(blank=False, null=False, default=False)
