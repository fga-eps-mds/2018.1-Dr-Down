from test_plus.test import TestCase
from django.test import RequestFactory
from django.test.client import Client


from ..models import Patient


class TestViewEmployee (TestCase):
    """
    Test if View Patient is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.client = Client()
        self.user = self.make_user()
        self.patient = Patient.objects.create(ses="1234567",
                                              user=self.user,
                                              mother_name="Mãe", father_name="Pai",
                                              ethnicity=3, sus_number="12345678911",
                                              civil_registry_of_birth="12345678911",
                                              declaration_of_live_birth="12345678911")

    def test_patient_get_context_data(self):
        """
        Makes sure that the patient data is showing at the user detail view
        """

        self.patient.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser/', follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(self.user.patient.ses, self.patient.ses)

        self.assertContains(response, text=self.user.username)
        self.assertContains(response, text=self.user.username)

        self.assertContains(response, text=self.user.patient.ses)
