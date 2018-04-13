from test_plus.test import TestCase
from django.test import RequestFactory
from django.test.client import Client


from ..models.model_doctor import Doctor


class TestViewDoctor (TestCase):
    """
    Test if View Doctor is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.client = Client()
        self.user = self.make_user()
        self.doctor = Doctor.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=Doctor.NEUROLOGY)

    def test_doctor_get_context_data(self):
        """
        Test if the view doctor is passing the data correctly
        """

        self.doctor.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser/', follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(self.user.doctor.cpf, self.doctor.cpf)

        self.assertContains(response, text=self.user.username)
        self.assertContains(response, text=self.user.username)

        self.assertContains(response, text=self.user.doctor.cpf)

    def test_doctor_get_context_data_error(self):
        """
        Test if the view doctor is not passing data in case of error
        """

        self.doctor.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser1/', follow=True)

        self.assertEquals(response.status_code, 404)
