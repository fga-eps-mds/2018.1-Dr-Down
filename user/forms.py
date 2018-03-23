from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        date_available = forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y"))

        model = User
        fields = ['name', 'last_name', 'email', 'password', 'birthday',
                  'gender', 'telephone']

        widgets = {
                    'password': forms.PasswordInput(),
                    }
