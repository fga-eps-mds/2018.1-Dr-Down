from django.db import models
from django.utils.translation import ugettext_lazy as _


class CheckItem(models.Model):

    procedure = models.ForeignKey('careline.Procedure', on_delete=models.CASCADE)

    # get age converted as identification code
    age = models.CharField(max_length=5, null=False, blank=False)

    required = models.BooleanField(blank=False, null=False, default=False)
    when_needed = models.BooleanField(blank=False, null=False, default=False)

    check = models.BooleanField(blank=False, null=False, default=False)
