from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'password', 'birthday',
                  'gender', 'telephone']
