from test_plus.test import TestCase
from drdown.users.models import User


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()


    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_short_name(self):

        self.assertEquals(self.user.get_short_name(),
        	self.user.first_name)

class TestField(TestCase):

    def setUp(self):
        """
        This method will run before any test.
        """

        self.superuser = User.objects.create_superuser(
            name='Ohaio',
            first_name='Ohaio',
            username='Ohaionini',
            email='ohaio@gmail.com',
            password='ohaio123456'
        )

        self.user1 = User.objects.create_user(
            first_name='Pedro',
            name='Pedro',
            username='pedro100',
            email='pedro@gmail.com',
            password='pedro123456'
        )

        self.user2 = User.objects.create_user(
            first_name='Jobs',
            name='Jobs',
            username='jobs101',
            email='jobs@gmail.com',
            password='jobs123456'
        )

    def tearDown(self):
        """
        This method will run after any test.
        """

        self.user1.delete()
        self.user2.delete()

    def test_short_name(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.user1.get_short_name(), self.user1.name)
        self.assertEquals(self.user2.get_short_name(), self.user2.name)






