from django.db import models
from .models import User

class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=True)
    crm = models.IntegerField(max_length=30, blank=True)
    speciality = models.CharField(max_length=50, blank=True)