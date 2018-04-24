from test_plus.test import TestCase
from django.test import RequestFactory
from django.test.client import Client


from ..models.model_health_team import HealthTeam


class TestViewHealthTeam (TestCase):
    """
    Test if View Health_Team is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.client = Client()
        self.user = self.make_user()
        self.health_team = HealthTeam.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=HealthTeam.NEUROLOGY)

    def test_health_team_get_context_data(self):
        """
        Test if the view health team is passing the data correctly
        """

        self.health_team.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser/', follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(self.user.healthteam.cpf, self.health_team.cpf)

        self.assertContains(response, text=self.user.username)
        self.assertContains(response, text=self.user.username)

        self.assertContains(response, text=self.user.healthteam.cpf)

