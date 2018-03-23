from django.test import TestCase, Client
from django.shortcuts import reverse

from user.models import User
# Create your tests here.


class UserViewTestCase(TestCase):
    def create_user(self, name="Joao", last_name="Silva",
                    email="user@example.com", password="12345678",
                    birthday="1997-01-01", gender="M",
                    telephone=12345678):
        return User.objects.create(name=name, last_name=last_name,
                                   email=email, password=password,
                                   birthday=birthday, gender=gender,
                                   telephone=telephone)

    def test_list_view(self):
        list_url = reverse("list_users")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_was_created_user(self):
        """
            was_created_user() tests if a user that was created appears
            on the correct view
        """
        # create a test Client and ask it to get our user page
        # note: at this moment our user page shows a list of created
        # users. This test will nedd to be changed when the view/html
        # is updated
        c = Client()
        response = c.get('/users/')

        # check if the user that will be created is NOT present on user list
        self.assertNotContains(response, "Test")

        # create a dummy user on our DB
        dummy_user = self.create_user(name="Test")

        # reload or user page
        response = c.get('/users/')

        # test the response to find if a user was created
        # it checks for the presence of a username on the response page
        self.assertContains(response, dummy_user.name)
