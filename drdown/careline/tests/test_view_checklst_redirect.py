from test_plus.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse
from django.utils import timezone

from drdown.careline.models import Procedure
from drdown.users.models import Patient, Responsible, Employee

from drdown.careline.views import ChecklistRedirectView


class TestViewChecklistRedirectView(TestCase):
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

    def test_redirect(self):

        self.client.force_login(self.user_responsible)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_list',
            ),
            follow=True
        )

        url = self.client.get(
            path=reverse(viewname='users:patient_list')
        ).url

        self.assertRedirects(response=response, expected_url=url)