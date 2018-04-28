from test_plus.test import TestCase

from drdown.careline.models import Checklist
from drdown.users.models.model_patient import Patient


class TestModelChecklistNoSetup(TestCase):
    """
        Test if model Checklist is working correctly (no setUp method)
    """

    def test_patient_creating_checklist(self):
        """
           Test if when a patient is created, it's creating its checklist
        """

        self.user_patient1 = self.make_user()

        self.patient1 = Patient(
            ses="1234567",
            user=self.user_patient1,
            priority=1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible=None
        )

        self.assertEqual(hasattr(self.patient1, 'checklist'), False)

        self.patient1.save()

        self.assertEqual(hasattr(self.patient1, 'checklist'), True)


class TestModelChecklist(TestCase):
    """
        Test if model Checlist is working correctly
    """

    def setUp(self):
        """
           This method will run before any test.
        """

        self.user_patient1 = self.make_user()

        self.patient1 = Patient.objects.create(
            ses="1234567",
            user=self.user_patient1,
            priority=1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible=None
        )

    def test_checklist_created_procedures_only_on_first_run(self):
        """
            Test if a checklist is creating its procedures only once
        """

        self.checklist = self.patient1.checklist

        self.assertEquals(
            hasattr(self.checklist, 'procedure_set'),
            True
        )

        self.checklist.save()

        self.assertEquals(
            self.checklist.procedure_set.all().count(),
            len(Checklist.CARE_LINE)
        )

        # if we save the checklist again, the amount of procedures should
        # remain the same

        self.checklist.save()

        self.assertEquals(
            self.checklist.procedure_set.all().count(),
            len(Checklist.CARE_LINE)
        )

