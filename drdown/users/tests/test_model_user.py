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
            last_name='Nini',
            first_name='Ohaio',
            username='Ohaionini',
            email='ohaio@gmail.com',
            password='ohaio123456',
            birthday='1998-03-05',
            telephone='(11)11111-1111',
            gender='M',
            created_at='2018-03-05',
            updated_at='2018-03-05',
            photo='example.jpg'
        )

        self.user1 = User.objects.create_user(
            first_name='Pedro',
            last_name='Victor',
            name='Pedro',
            username='pedro100',
            email='pedro@gmail.com',
            password='pedro123456',
            birthday='1998-04-05',
            telephone='(22)22222-2222',
            gender='F',
            created_at='2018-04-05',
            updated_at='2018-04-05',
            photo='example.jpg'
        )

        self.user2 = User.objects.create_user(
            first_name='Jobs',
            last_name='Rogers',
            name='Jobs',
            username='jobs101',
            email='jobs@gmail.com',
            password='jobs123456',
            birthday='1998-05-05',
            telephone='(33)33333-3333',
            gender='M',
            created_at='2018-05-05',
            updated_at='2018-05-05',
            photo='example.jpg'
        )

    def tearDown(self):
        """
        This method will run after any test.
        """

        self.superuser.delete()
        self.user1.delete()
        self.user2.delete()

    def test_short_name(self):
        """
        Test to get the full name of user
        """
        self.assertEquals(self.superuser.get_short_name(), self.superuser.name)
        self.assertEquals(self.user1.get_short_name(), self.user1.name)
        self.assertEquals(self.user2.get_short_name(), self.user2.name)


    def test_name(self):
        """
        Test to get the full name of user
        """
        self.assertEquals( self.superuser.name, 'Ohaio')
        self.assertEquals( self.user1.name, 'Pedro')
        self.assertEquals(self.user2.name, 'Jobs')


    def test_invalid_name(self):
        """
        Test to get the full name of user
        """
        self.assertNotEquals( self.superuser.name, '')
        self.assertNotEquals( self.user1.name, '')
        self.assertNotEquals(self.user2.name, '')

    def test_first_name(self):
        """
        Test to get the full name of user
        """
        self.assertEquals( self.superuser.first_name, 'Ohaio')
        self.assertEquals( self.user1.first_name, 'Pedro')
        self.assertEquals(self.user2.first_name, 'Jobs')


    def test_invalid_first_name(self):
        """
        Test to get the full name of user
        """
        self.assertNotEquals( self.superuser.first_name, '')
        self.assertNotEquals( self.user1.first_name, '')
        self.assertNotEquals(self.user2.first_name, '')


    def test_last_name(self):
        """
        Test to get the full name of user
        """
        self.assertEquals( self.superuser.last_name, 'Nini')
        self.assertEquals( self.user1.last_name, 'Victor')
        self.assertEquals(self.user2.last_name, 'Rogers')


    def test_invalid_last_name(self):
        """
        Test to get the full name of user
        """
        self.assertNotEquals( self.superuser.last_name, '')
        self.assertNotEquals( self.user1.last_name, '')
        self.assertNotEquals(self.user2.last_name, '')


    def test_birthday(self):
        """
        Test for verify if the birthday is the same for compare
        """
        self.assertEquals( self.superuser.birthday, '1998-03-05')
        self.assertEquals(self.user1.birthday, '1998-04-05')
        self.assertEquals(self.user2.birthday, '1998-05-05')

    def test_in_not_birthday(self):
        """
        Test for verify if the birthday is the same for compare
        """
        self.assertNotEquals( self.superuser.birthday, '')
        self.assertNotEquals(self.user1.birthday, '')
        self.assertNotEquals(self.user2.birthday, '')

    def test_telephone(self):
        """
        Test for verify if the phone is the same for compare
        """
        self.assertEquals( self.superuser.telephone, '(11)11111-1111')
        self.assertEquals(self.user1.telephone, '(22)22222-2222')
        self.assertEquals(self.user2.telephone, '(33)33333-3333')

    def test_is_not_telephone(self):
        """
        Test for verify if the phone is the same for compare
        """
        self.assertNotEquals( self.superuser.telephone, '')
        self.assertNotEquals(self.user1.telephone, '')
        self.assertNotEquals(self.user2.telephone, '')

    def test_email(self):
        """
        Test for verify if the phone is the same for compare
        """
        self.assertEquals( self.superuser.email, 'ohaio@gmail.com')
        self.assertEquals(self.user1.email, 'pedro@gmail.com')
        self.assertEquals(self.user2.email, 'jobs@gmail.com')

    def test_is_not_email(self):
        """
        Test for verify if the phone is the diferent for compare
        """
        self.assertNotEqual( self.superuser.email, '')
        self.assertNotEqual(self.user1.email, '')
        self.assertNotEqual(self.user2.email, '')

    def test_gender(self):
        """
        Teste for verify if the gender is the same of compare
        """

        self.assertEquals( self.superuser.gender, 'M')
        self.assertEquals(self.user1.gender, 'F')
        self.assertEquals(self.user2.gender, 'M')

    def test_created_at(self):
        """
        Test for verify if the create_at is the same for compare
        """
        self.assertEquals( self.superuser.created_at, '2018-03-05')
        self.assertEquals(self.user1.created_at, '2018-04-05')
        self.assertEquals(self.user2.created_at, '2018-05-05')

    def test_in_not_creted_at(self):
        """
        Test for verify if the create_at is diferent for compare
        """
        self.assertNotEquals( self.superuser.created_at, '')
        self.assertNotEquals(self.user1.created_at, '')
        self.assertNotEquals(self.user2.created_at, '')

    def test_updated_at(self):
        """
        Test for verify if the update_at is the same for compare
        """
        self.assertEquals( self.superuser.updated_at, '2018-03-05')
        self.assertEquals(self.user1.updated_at, '2018-04-05')
        self.assertEquals(self.user2.updated_at, '2018-05-05')

    def test_in_not_updated_at(self):
        """
        Test for verify if the update_at is the diferent for compare
        """
        self.assertNotEquals( self.superuser.updated_at, '')
        self.assertNotEquals(self.user1.updated_at, '')
        self.assertNotEquals(self.user2.updated_at, '')

    def test_photo(self):

         self.assertEquals( self.superuser.photo, 'example.jpg')
         self.assertEquals(self.user1.photo, 'example.jpg')
         self.assertEquals(self.user2.photo, 'example.jpg')

    def test_photo(self):

         self.assertNotEquals( self.superuser.photo, '')
         self.assertNotEquals(self.user1.photo, '')
         self.assertNotEquals(self.user2.photo, '')













