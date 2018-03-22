from django.test import TestCase, Client
from django.shortcuts import reverse

from user.models import User


def create_dummy_user(
    email="testuser@testmail.com",
    password="dummypass",
    name="Test",
    last_name="User",
    birthday="2000-01-01",
    gender="M",
    telephone="99999999999"
):
    """
        creates dummy user for tests (options can be overriden on
        function call)
    """

    return User.objects.create(
         email=email,
         password=password,
         name=name,
         last_name=last_name,
         birthday=birthday,
         gender=gender,
         telephone=telephone
        )


class UserViewsTests(TestCase):

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
        response = c.get('')

        # check if the user that will be created is NOT present on user list
        self.assertNotContains(response, "Test")

        # create a dummy user on our DB
        dummy_user = create_dummy_user(name="Test")

        # reload or user page
        response = c.get('')

        # test the response to find if a user was created
        # it checks for the presence of a username on the response page
        self.assertContains(response, dummy_user.name)
