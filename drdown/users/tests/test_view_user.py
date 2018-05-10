from django.test import RequestFactory
from django.urls import reverse_lazy
from django.test.client import Client
from django.urls import reverse
from django.utils import timezone
from test_plus.test import TestCase
from ..models import (
    User, Responsible, Employee,
    HealthTeam, Patient
)
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


class TestPatientListViewSelector(TestCase):
    """
        Test if the Selector of List View of user is working correctly
    """

    def setUp(self):
        """
            Runs before every test
        """

        self.user_responsible = self.make_user(username='resp')

        self.user_responsible.birthday = timezone.datetime(1950, 1, 1)

        self.user_responsible.save()
        self.user_responsible.refresh_from_db()

        Responsible.objects.create(
            user=self.user_responsible,
            cpf="974.220.200-16"
        )

        self.user_patient1 = self.make_user(username='pat1')

        self.user_patient1.birthday = timezone.datetime(2000, 1, 1)

        self.user_patient1.save()
        self.user_patient1.refresh_from_db()

        Patient.objects.create(
            ses="1234567",
            user=self.user_patient1,
            priority=1,
            mother_name="Mae",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible=self.user_responsible.responsible
        )

        self.user_patient1.refresh_from_db()

        self.user_patient2 = self.make_user(username='pat2')

        self.user_patient2.birthday = timezone.datetime(2000, 1, 1)

        self.user_patient2.save()
        self.user_patient2.refresh_from_db()

        Patient.objects.create(
            ses="1234213",
            user=self.user_patient2,
            priority=1,
            mother_name="Mae",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345633912",
            civil_registry_of_birth="12345123911",
            declaration_of_live_birth="1212338911",
            responsible=self.user_responsible.responsible
        )

        self.user_health_team = self.make_user()
        self.user_health_team.birthday = timezone.datetime(2000, 1, 1)

        self.user_health_team.save()
        self.user_health_team.refresh_from_db()

        self.health_team = HealthTeam.objects.create(
            cpf="057.641.271-65",
            user=self.user_health_team,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.user_employee = self.make_user(username="empl")
        self.user_employee.birthday = timezone.datetime(2000, 1, 1)

        self.user_employee.save()
        self.user_employee.refresh_from_db()

        self.employee = Employee.objects.create(
            cpf="057.641.271-65",
            user=self.user_employee
        )

        self.client = Client()

    def test_get_redirect_for_patient(self):
        """
            Test if a patient is redirected for its medical follow-up sheet when accessing the  List View
        """

        self.client.force_login(self.user_patient1)

        response = self.client.get(
            path=reverse(
                viewname='users:patient_list',
            ),
            follow=True
        )

        url = reverse(
            viewname='users:patient_medical_sheet',
            kwargs={'username': self.user_patient1.username}
        )

        self.assertRedirects(response=response, expected_url=url)

    def test_get_redirect_for_not_authenticated(self):
        """
            Test if a not authenticated user is redirected to login screen
        """

        response = self.client.get(
            path=reverse(
                viewname='users:patient_list',
            ),
            follow=True
        )

        url = reverse(viewname='account_login')

        self.assertRedirects(response=response, expected_url=url)

    def test_get_redirect_for_other_specializations_or_no_specialization(self):
        """
            Test if a user that is not specialized is redirected for its profile
            when accessing Checklist List View
        """

        user = self.make_user(username='nope')
        user.birthday = timezone.datetime(1950, 1, 1)
        user.save()

        self.client.force_login(user)

        response = self.client.get(
            path=reverse(viewname='careline:checklist_list')
        )

        expected_status_codes = [301, 302]

        self.assertIn(
            response.status_code,
            expected_status_codes
        )

        response = self.client.get(
            path=reverse(viewname='users:healthteam_patient_list')
        )

        expected_status_codes = [301, 302]

        self.assertIn(
            response.status_code,
            expected_status_codes
        )

        response = self.client.get(
            path=reverse(viewname='users:responsible_patient_list')
        )

        expected_status_codes = [301, 302]

        self.assertIn(
            response.status_code,
            expected_status_codes
        )


    def test_get_redirect_for_healthteam(self):
        """
            Test if the page loads when a health team
            is the current user
        """

        self.client.force_login(self.user_health_team)

        response = self.client.get(
            path=reverse(
                viewname='users:patient_list',
            ),
            follow=True
        )

        url = reverse(viewname='users:healthteam_patient_list')

        self.assertRedirects(response=response, expected_url=url)


    def test_get_redirect_for_employee(self):
        """
            Test if the page loads when a employee
            is the current user
        """

        self.client.force_login(self.user_employee)

        response = self.client.get(
            path=reverse(
                viewname='users:patient_list',
            ),
            follow=True
        )

        url = reverse(viewname='users:healthteam_patient_list')

        self.assertRedirects(response=response, expected_url=url)


    def test_get_redirect_for_responsible(self):
        """
            Test if the page loads when a responsible is the current user
        """

        self.client.force_login(self.user_responsible)

        response = self.client.get(
            path=reverse(
                viewname='users:patient_list',
            ),
            follow=True
        )

        url = reverse(viewname='users:responsible_patient_list')

        self.assertRedirects(response=response, expected_url=url)
