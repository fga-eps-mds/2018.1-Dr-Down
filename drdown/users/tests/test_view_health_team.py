from test_plus.test import TestCase
from django.test import RequestFactory
from django.test.client import Client


from ..models.model_health_team import Health_Team


class TestViewHealth_Team (TestCase):
    """
    Test if View Health_Team is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.client = Client()
        self.user = self.make_user()
        self.health_team = Health_Team.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=Health_Team.NEUROLOGY)

    def test_health_team_get_context_data(self):
        """
        Test if the view health team is passing the data correctly
        """

        self.health_team.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser/', follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(self.user.health_team.cpf, self.health_team.cpf)

        self.assertContains(response, text=self.user.username)
        self.assertContains(response, text=self.user.username)

        self.assertContains(response, text=self.user.health_team.cpf)

    def test_health_team_get_context_data_error(self):
        """
        Test if the view health team is not passing data in case of error
        """

        self.health_team.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser1/', follow=True)

        self.assertEquals(response.status_code, 404)
