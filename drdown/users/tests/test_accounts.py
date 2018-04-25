from django.conf import settings
from ..adapters import AccountAdapter
from ..adapters import SocialAccountAdapter
from django.urls import reverse
from test_plus.test import TestCase
from ..models import User
from django.test.client import Client


class AccountsTestCase(TestCase):

    def setUp(self):
        """
        This method will run before any test.
        """
        self.user = User.objects.create_user(username='test', password='12345')
        self.login_url = reverse('account_login')
        self.client = Client()

    def test_login(self):
        """
        Test login
        """
        response = self.client.post(self.login_url, {'username': 'test', 'password': '12345'})
        self.assertEquals(response.status_code, 200)

    def login_successful(self):

        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertTrue(not response.wsgi_request.user.is_authenticated())
        data = {'username': 'test', 'password': '12345'}
        response = self.client.post(self.login_url, data)
        redirect_url = reverse(AccountAdapter.get_login_redirect_url(self.request))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_account_is_open_for_sign_up(self):
        """
        Test if sign up is open
        """
        self.assertEqual(
            True,
            AccountAdapter.is_open_for_signup(AccountAdapter),
        )
        self.assertEqual(
            True,
            SocialAccountAdapter.is_open_for_signup(SocialAccountAdapter),
        )
