from test_plus.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse
from django.utils import timezone

from drdown.careline.models import Procedure
from drdown.users.models import Patient, Responsible, Employee

from drdown.careline.views import ChecklistListView


class TestViewChecklistListView(TestCase):
    """
        Test if the List View of Checklist is working correctly
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

        self.client = Client()
        self.view = ChecklistListView()

    def test_get_redirect_for_patient(self):
        """
            Test if a patient is redirected for its checklist when accessing Checklist List View
        """

        self.client.force_login(self.user_patient1)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_list',
            ),
            follow=True
        )

        url = reverse(viewname='careline:checklist_detail', kwargs={'username': self.user_patient1.username})

        self.assertRedirects(response=response, expected_url=url)

    def test_get_redirect_for_not_authenticated(self):
        """
            Test if a not authenticated user is redirected to login screen
        """

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_list',
            ),
            follow=True
        )

        url = reverse(viewname='account_login')

        self.assertRedirects(response=response, expected_url=url)

    def test_get_redirect_for_other_specializations_or_no_specialization(self):
        """
            Test if a user that is not patient or responsible is redirected for its profile
            when accessing Checklist List View
        """

        user = self.make_user(username='nope')
        user.birthday = timezone.datetime(1950, 1, 1)
        user.save()

        self.client.force_login(user)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_list',
            ),
            follow=True
        )

        url = reverse(viewname='users:detail', kwargs={'username': user.username})

        self.assertRedirects(response=response, expected_url=url)

        Employee.objects.create(
            cpf="306.585.340-09",
            user=user
        )

        user.refresh_from_db()

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_list',
            ),
            follow=True
        )

        url = reverse(viewname='users:detail', kwargs={'username': user.username})

        self.assertRedirects(response=response, expected_url=url)

    def test_get_page_when_responsible(self):
        """
            Test if the page loads when a responsible is the current user
        """

        self.client.force_login(self.user_responsible)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_list',
            ),
            follow=True
        )

        self.assertEquals(response.status_code, 200)
