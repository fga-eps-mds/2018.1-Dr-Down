from django.test import RequestFactory
from django.urls import reverse_lazy
from django.test.client import Client
from django.urls import reverse
from test_plus.test import TestCase
from ..models import User
from ..views import (
    UserRedirectView,
    UserUpdateView
)


class BaseUserTestCase(TestCase):
    """
    Test if BasedUser is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """
        self.user = self.make_user()
        self.factory = RequestFactory()


class TestUserRedirectView(BaseUserTestCase):

    def test_get_redirect_url(self):
        # Instantiate the view directly. Never do this outside a test!
        view = UserRedirectView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        view.request = request
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            view.get_redirect_url(),
            '/users/testuser/'
        )


class TestUserUpdateView(BaseUserTestCase):

    def setUp(self):
        """
        This method will run before any test.
        """
        # call BaseUserTestCase.setUp()
        super(TestUserUpdateView, self).setUp()
        # Instantiate the view directly. Never do this outside a test!
        self.view = UserUpdateView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        self.view.request = request

    def test_get_success_url(self):
        """
        Expect: '/users/testuser/', as that is the default username for
        """

        self.assertEqual(
            self.view.get_success_url(),
            '/users/testuser/'
        )

    def test_get_object(self):
        """
        Expect: self.user, as that is the request's user object
        """

        self.assertEqual(
            self.view.get_object(),
            self.user
        )


class TestUserDeleteView(BaseUserTestCase):

    def setUp(self):
        """
        This method will run before any test.
        """

        super(TestUserDeleteView, self).setUp()
        self.url = reverse_lazy('users:delete')
        self.client = Client()

    def tearDownUser(self):
        """
        This method will run after any test.
        """

        self.user.delete()

    def test_delete_user_ok(self):
        """
        Test is user is being correcty deleted.
        """
        self.assertEquals(User.objects.count(), 1)

        self.client.force_login(user=self.user)

        response = self.client.post(self.url, follow=True)

        home_url = reverse_lazy('core:home')

        self.assertRedirects(response, home_url)

        self.assertEquals(User.objects.count(), 0)


class TestUserDetailView(BaseUserTestCase):

    def setUp(self):
        """
        This method will run before any test.
        """
        self.user = self.make_user()
        self.second_user = self.make_user('testuser2')

    def test_logged_user_redirect_detail_view(self):
        """
        Test if view is redirected if user is not logged in user
        """
        self.client.force_login(user=self.user)

        login_url = reverse(
            viewname='users:detail',
            kwargs={'username': self.second_user.username}
        )

        response = self.client.get(path=login_url, follow=True)

        self.assertEquals(response.status_code, 200)

    def test_not_logged_user_redirect_detail_view(self):
        """
        Test if view is redirected if user is not logged in
        """

        login_url = reverse(
            viewname='users:detail',
            kwargs={'username': self.second_user.username}
        )

        response = self.client.get(path=login_url, follow=True)

        self.assertEquals(response.status_code, 200)

