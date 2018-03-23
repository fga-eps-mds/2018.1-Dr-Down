from django.test import TestCase
from user.forms import UserForm
from user.models import User


class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(name="Joao", last_name="Silva",
                                        email="user@example.com",
                                        password="12345678",
                                        birthday="01/01/1997", gender="M",
                                        telephone=12345678)


class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'name': "Joao", 'last_name': "Silva",
                              'email': "user@example.com",
                              'password': "12345678",
                              'birthday': "01/01/1997", 'gender': "M",
                              'telephone': 12345678})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'name': "", 'last_name': "",
                              'email': "", 'password': "",
                              'birthday': "", 'gender': "",
                              'telephone': 12345678})
        self.assertFalse(form.is_valid())
