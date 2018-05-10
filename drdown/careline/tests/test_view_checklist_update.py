from test_plus.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse
from django.utils import timezone

from drdown.careline.models import Procedure
from drdown.users.models import Patient, Responsible, Employee

from drdown.careline.views import ChecklistUpdateView

class TestViewChecklistListView(TestCase):
    """
        Test if the Update View of Checklist is working correctly
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
        self.view = ChecklistUpdateView()

    def test_get_redirect(self):
        """
            Test if view is redirecting
        """

        self.client.force_login(user=self.user_responsible)

        response = self.client.get(
            reverse(viewname="careline:checklist_update")
        )

        expected_status_codes = [301, 302]

        self.assertIn(
            response.status_code,
            expected_status_codes
        )

    def test_process_change(self):
        """
            Assert that checkitem is beeing changed
        """

        procedure = list(self.user_patient1.patient.checklist.procedure_set.all()).pop(0)
        procedure_id = procedure.id

        checkitem = list(procedure.checkitem_set.all()).pop(0)
        checkitem_id = checkitem.id

        self.assertFalse(checkitem.check)

        self.view.process_change(
            user=self.user_patient1,
            checklist_id=checkitem_id,
            procedure_id=procedure_id,
            value=True
        )

        checkitem.refresh_from_db()

        self.assertTrue(checkitem.check)

    def test_has_permission(self):
        """
            Test if has permission is respecting rules
        """

        # since the ChecklistDetailView.has_permission is already tested,
        # we will only test for age

        # patient has less than 13 years
        self.user_patient1.birthday = timezone.datetime.today() - timezone.timedelta(days=365*10)
        self.user_patient1.save()

        self.assertEquals(
            self.view.has_permission(current_user=self.user_patient1, target_user=self.user_patient1),
            False
        )

        # patient has more than 13 years
        self.user_patient1.birthday = timezone.datetime.today() - timezone.timedelta(days=365 * 14)
        self.user_patient1.save()

        self.assertEquals(
            self.view.has_permission(current_user=self.user_patient1, target_user=self.user_patient1),
            True
        )

    def test_post(self):
        """
            Checks if post is working properly
        """

        self.client.force_login(user=self.user_patient1)

        procedure = list(
            self.user_patient1.patient.checklist.procedure_set.all()
        ).pop(0)
        procedure_id = procedure.id

        checkitem = list(procedure.checkitem_set.all()).pop(0)
        checkitem_id = checkitem.id

        self.assertFalse(checkitem.check)

        url = reverse(viewname="careline:checklist_update")

        post_args = {
            'username': self.user_patient1.username,
            'checklist_id': checkitem_id,
            'procedure_id': procedure_id,
            'value': 1  # using number, because real request uses it
        }

        self.client.post(path=url, data=post_args)

        checkitem.refresh_from_db()

        self.assertTrue(checkitem.check)

        post_args.update({'value': 0})

        self.user_patient1.birthday = timezone.datetime.today() - timezone.timedelta(days=365 * 5)
        self.user_patient1.save()

        self.response_403(self.client.post(path=url, data=post_args))
        self.assertTrue(checkitem.check)

        self.client = Client()

        hacker_user = self.make_user(username="hacker")
        hacker_user.birthday = timezone.datetime.today() - timezone.timedelta(days=365 * 15)
        hacker_user.save()

        self.client.force_login(hacker_user)

        self.response_403(self.client.post(path=url, data=post_args))
        self.assertTrue(checkitem.check)

        self.client = Client()
