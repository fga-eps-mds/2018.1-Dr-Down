from django.test import TestCase, Client
from django.shortcuts import reverse
from user.models import User


class UserViewTestCase(TestCase):

    def test_create_users(self):

            self.client = Client()
            user = User.objects.create(name='joao', last_name='per1',
                                       email='person1@gmail.com',
                                       password='test',
                                       birthday='2016-05-05',
                                       gender='M',
                                       telephone='1234567')

            self.assertEquals(User.objects.count(), 1)

            user2 = User.objects.create(name='aluno', last_name='per2',
                                        email='person2@gmail.com',
                                        password='test2',
                                        birthday='2012-02-02',
                                        gender='M',
                                        telephone='1234567')

            self.assertEquals(User.objects.count(), 2)

    def test_list_view(self):
        """

        This test is valid when the view list user part is work
        """

        list_url = reverse("list_users")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_with_invalid_email(self):
        """
        Test that verify if email correspond with erro if no add
        """

        data = {
            'name': 'person',
            'last_name': 'test',
            'email': 'alsda@dskal.com',
            'password': 'test2',
            'birthday': '2012-02-02',
            'gender': 'M',
            'telephone': '1234567'

        }

        response = self.client.post(reverse('create_user'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_user_was_updated(self):
        """
            test if the user updated was successful after
            an update procedure using the update user form
        """

        c = Client()

        # create user in db
        user = self.create_user()

        initial_name = user.name

        # assert presence of user on user list
        self.assertContains(c.get('/users/'), user.name)

        # lets change all data
        data = {
            'birthday': "1998-01-01",
            'email': "notuser@notmail.notcom",
            'gender': "F",
            'last_name': "NotLastName",
            'name': "NotName",
            'password': "supersecurepassword1203i",
            'telephone': 12345678
        }

        # POST the changes
        response = c.post('/users/edit/' + str(user.id), data=data)

        self.assertEqual(response.status_code, 302)

        user.refresh_from_db()

        # some tests need a str() conversion before the assertion

        self.assertEquals(user.name, data['name'])
        self.assertEqual(user.last_name, data['last_name'])

        self.assertEqual(str(user.birthday), data['birthday'])
        self.assertEqual(user.gender, data['gender'])
        self.assertEqual(user.telephone, str(data['telephone']))

        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.password, data['password'])

        self.assertContains(c.get('/users/'), data['name'])
        self.assertNotContains(c.get('/users/'), initial_name)
