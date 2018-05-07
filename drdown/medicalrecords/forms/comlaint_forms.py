from drdown.medicalrecords.models.model_complaint import Complaint
from django import forms
from pagedown.widgets import PagedownWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget


class ComplaintForm(forms.ModelForm):

    description = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Complaint
        fields = ["description", "complaint_day"]
