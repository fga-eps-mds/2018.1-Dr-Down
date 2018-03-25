from django.test import TestCase, Client
from user.models import User
from django.shortcuts import reverse


class DeleteUserTest(TestCase):

    def setUp(self):
        """
        This method creates a user for testing.
        """
        self.url = reverse('delete_user', kwargs={'pk': 1})
        self.user = User.objects.create(name="Joao", last_name="Silva",
                                        email="user@example.com", password="12345678",
                                        birthday="1997-01-01", gender="M",
                                        telephone=12345678)

    def tearDownUser(self):
        """
        This method will run after any test.
        """

        self.user.delete()

    def test_delete_user(self):
        """
        Test to delete user with success.
        """

        self.assertEquals(User.objects.count(), 1)
        self.client.login(name=self.user.name, password='12345678')
        response = self.client.post(self.url, follow=True)
        home_url = reverse('list_users')
        self.assertRedirects(response, home_url)
        self.assertEquals(User.objects.count(), 0)
