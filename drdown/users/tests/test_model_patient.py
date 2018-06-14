from test_plus.test import TestCase
from ..admin import PatientAdmin
from ..models import Patient, Responsible
from ..models.model_patient import careline_notification

from django.db.models import Q
from django.utils import timezone


class TestModelPatient(TestCase):
    """
    Test if model Patient is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user = self.make_user()

        self.user.birthday = timezone.datetime(year=2000, month=1, day=1)
        self.user.email = "not@an.email"

        self.user.save()
        self.user.refresh_from_db()

        self.user1 = self.make_user(username="user1")

        self.user1.birthday = timezone.datetime(year=2000, month=1, day=1)
        self.user1.email = "not@another.email"

        self.user1.save()
        self.user1.refresh_from_db()

        self.responsible = Responsible.objects.create(
            cpf="974.220.200-16",
            user=self.user1
        )

        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible=self.responsible
        )

    def test_get_absolute_url(self):
        """
        This test will get the absolute url of user.
        """

        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_one_to_one_relation(self):
        """
        This test will check if the one_to_one relation is being respected.
        """

        self.assertIs(self.user, self.patient.user)
        self.assertIs(self.patient, self.user.patient)

    def test_delete_cascade(self):
        """
        This test check if all object data is deleted along with it.
        """

        self.assertEquals(Patient.objects.get(ses="1234567"), self.patient)

        self.user.delete()

        with self.assertRaises(Patient.DoesNotExist):
            Patient.objects.get(ses="1234567")

    def test__str__(self):
        """
        This test check if __str__ is returning the data correctly.
        """

        self.assertEqual(
            self.patient.__str__(),
            self.user.get_username()
        )

    def test_readonly_user(self):
        """
        Test is user field is read_only after creation of an patient
        """

        ma = PatientAdmin(model=Patient, admin_site=None)

        # since there is no atribute patient in self user, we
        # can assume that obj=None
        self.assertEqual(
            list(ma.get_readonly_fields(self, obj=None)),
            []
        )

        self.assertEqual(
            hasattr(self.user, 'patient'),
            True
        )

        ma1 = PatientAdmin(model=Patient, admin_site=None)
        self.assertEqual(
            list(ma1.get_readonly_fields(self, obj=self.user.patient)),
            ['user']
        )

    def test_birthday_is_close(self):
        """
            Test if response is accurate based on patient birthday
        """

        today = timezone.datetime.today()

        self.user.birthday = today - timezone.timedelta(days=365 + 29)

        self.assertEquals(
            self.user.patient.birthday_is_close(),
            True
        )

        self.user.birthday = today - timezone.timedelta(days=365 + 30)

        self.assertEquals(
            self.user.patient.birthday_is_close(),
            True
        )

        self.user.birthday = today - timezone.timedelta(days=365 + 31)

        self.assertEquals(
            self.user.patient.birthday_is_close(),
            False
        )

    def test_have_incomplete_procedures_on_current_age(self):
        """
            Test if method produces correct response based on patient checklist
        """

        checklist = self.user.patient.checklist

        for procedure in checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = True
                check_item.save()

        checklist.refresh_from_db()

        self.assertEquals(
            self.user.patient.have_incomplete_procedures_on_current_age(),
            False
        )

        for procedure in checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = False
                check_item.save()

        checklist.refresh_from_db()

        self.assertEquals(
            self.user.patient.have_incomplete_procedures_on_current_age(),
            True
        )

    def test_have_procedures_almost_late(self):
        """
            Test if method produces correct response based on patient checklist
        """

        today = timezone.datetime.today()

        self.user.birthday = today - timezone.timedelta(days=365 + 29)

        checklist = self.user.patient.checklist

        for procedure in checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = True
                check_item.save()

        checklist.refresh_from_db()

        self.assertEquals(
            self.user.patient.have_procedures_almost_late(),
            False
        )

        for procedure in checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = False
                check_item.save()

        checklist.refresh_from_db()

        self.assertEquals(
            self.user.patient.have_procedures_almost_late(),
            True
        )

    def test_count_incomplete_procedures_for_current_age(self):
        """
            Test if method produces correct response based on patient checklist
        """

        from drdown.careline.models.model_procedure import Procedure

        today = timezone.datetime.today()

        self.user.birthday = today - timezone.timedelta(days=365 + 29)
        self.user.save()
        self.user.refresh_from_db()

        checklist = self.user.patient.checklist

        for procedure in checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = True
                check_item.save()

        checklist.refresh_from_db()

        self.assertEquals(
            self.user.patient.count_incomplete_procedures_for_current_age(),
            0
        )

        for procedure in checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = False
                check_item.save()

        checklist.refresh_from_db()

        itens_age = Procedure.convert_age_to_item(self.user.age())

        itens_count = self.user.patient.checklist.procedure_set.filter(
            Q(checkitem__required=True) | Q(checkitem__when_needed=True),
            checkitem__age=itens_age,
            checkitem__check=False,
        ).count()

        self.assertEquals(
            self.user.patient.count_incomplete_procedures_for_current_age(),
            itens_count
        )

    def test_careline_notifications(self):
        """
            Test if patients are correct in careline notifications
        """

        target_patients = careline_notification()

        self.assertIn(self.patient, target_patients)

        for procedure in self.patient.checklist.procedure_set.all():
            for check_item in procedure.checkitem_set.all():
                check_item.check = True
                check_item.save()

        target_patients = careline_notification()

        self.assertNotIn(self.patient, target_patients)
