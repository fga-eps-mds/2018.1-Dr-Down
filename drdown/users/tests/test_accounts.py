from django.conf import settings
from ..adapters import AccountAdapter
from ..adapters import SocialAccountAdapter
from django.urls import reverse
from test_plus.test import TestCase
from ..models import User
from django.test.client import Client
from django.utils.timezone import now
from django.urls import reverse
from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible

class AccountsTestCase(TestCase):

    def setUp(self):
        """
        This method will run before any test.
        """
        self.user = User.objects.create_user(username='test', password='12345')
        self.login_url = reverse('account_login')
        self.client = Client()
        self.user2 = self.user = User.objects.create_user(
            username='mariam', password='12345', name='Maria')
        self.user3 = self.user = User.objects.create_user(
            username='joao', password='12345')
        self.user_1 = self.user = User.objects.create_user(
            username='felipe', password='12345', name='lipe')
        self.user_2 = self.user = User.objects.create_user(
            username='mam', password='12345', name='Mam')
        self.user_3 = self.user = User.objects.create_user(
            username='lol', password='12345', name='lol')
        self.user_4 = self.user = User.objects.create_user(
            username='sab', password='12345', name='sab')


        self.responsible = Responsible.objects.create(
            user=self.user_3,
            cpf="065.770.581-05",
        )

        self.patient = Patient.objects.create(ses="1234567",
                                              user=self.user_2,
                                              mother_name="Mãe",
                                              father_name="Pai",
                                              ethnicity=3,
                                              responsible=self.responsible,
                                              sus_number="123456789012345",
                                              civil_registry_of_birth="12345678911",
                                              declaration_of_live_birth="12345678911")

        self.health_team = HealthTeam.objects.create(
            cpf="507.522.730-94",
            user=self.user_1,
            council_acronym='CRM',
            register_number=123456789,
            registration_state='DF',
            speciality=HealthTeam.NEUROLOGY
        )

        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user_4,
            departament=Employee.ADMINISTRATION
        )

    def test_login(self):
        """
        Test login
        """
        response = self.client.post(
            self.login_url, {'username': 'test', 'password': '12345'})
        self.assertEquals(response.status_code, 200)

    def login_successful(self):

        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertTrue(not response.wsgi_request.user.is_authenticated())
        data = {'username': 'test', 'password': '12345'}
        response = self.client.post(self.login_url, data)
        redirect_url = reverse(
            AccountAdapter.get_login_redirect_url(self.request))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_account_is_open_for_sign_up(self):
        """
        Test if sign up is open
        """
        self.assertEqual(
            True,
            AccountAdapter.is_open_for_signup(AccountAdapter, self.request),
        )
        self.assertEqual(
            True,
            SocialAccountAdapter.is_open_for_signup(
                SocialAccountAdapter, self.request),
        )

    def test_redirect_login_sucess(self):
        self.client.force_login(user=self.user2)
        user_redirect = self.client.post('/accounts/login/')
        detail_view = reverse('users:detail', kwargs={
                              'username': self.user2.username})
        self.assertRedirects(user_redirect, detail_view)

    def test_redirect_login_sucess_patient(self):
        self.client.force_login(user=self.user_2)
        user_redirect = self.client.post('/accounts/login/')
        patient_view = reverse('notifications:patient_notifications')
        self.assertRedirects(user_redirect, patient_view)

    def test_redirect_login_sucess_responsible(self):
        self.client.force_login(user=self.user_3)
        user_redirect = self.client.post('/accounts/login/')
        responsible_view = reverse('notifications:responsible_notifications')
        self.assertRedirects(user_redirect, responsible_view)

    def test_redirect_not_logged_sucess(self):
        self.client.force_login(user=self.user3)
        user_redirect = self.client.post('/accounts/login/')
        update_view = reverse('users:update')
        self.assertRedirects(user_redirect, update_view)



    def test_email_confirmation_redirects(self):
        user = self.user
        email = EmailAddress.objects.create(
            user=user,
            email='a@b.com',
            verified=False,
            primary=True
        )
        self.client.force_login(user=user)
        confirmation = EmailConfirmation.create(email)
        confirmation.sent = now()
        confirmation.save()
        url_from = self.client.post(
            reverse(
                viewname='account_confirm_email',
                args=[confirmation.key]
            )
        )
        url_to = AccountAdapter.get_email_confirmation_redirect_url(
            AccountAdapter,
            self.request,
        )
        self.assertRedirects(
            url_from,
            url_to,
            fetch_redirect_response=False
        )
