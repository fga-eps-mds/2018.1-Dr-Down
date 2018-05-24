from test_plus.test import TestCase
from django.test import RequestFactory
from django.test.client import Client


from ..models import Responsible, Patient


class TestViewEmployee (TestCase):
    """
    Test if View Employee is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.client = Client()
        self.user_1 = self.make_user()
        self.user_2 = self.make_user(username="teste_2")
        self.patient = Patient.objects.create(ses="1234567",
                                              user=self.user_2,
                                              mother_name="Mãe", father_name="Pai",
                                              ethnicity=3, sus_number="12345678911",
                                              civil_registry_of_birth="12345678911",
                                              declaration_of_live_birth="12345678911")

        self.responsible = Responsible.objects.create(cpf="974.220.200-16", patient=self.patient, user=self.user_1)

    def test_responsible_get_context_data(self):
        """
        Makes sure that the employee data is showing at the user detail view
        """

        self.responsible.save()
        self.client.force_login(user=self.user_1)

        response = self.client.get(path='/users/testuser/', follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(self.user_1.responsible.cpf, self.responsible.cpf)

        self.assertContains(response, text=self.user_1.username)
        self.assertContains(response, text=self.user_1.username)

        self.assertContains(response, text=self.user_1.responsible.cpf)
