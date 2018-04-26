from test_plus.test import TestCase

from drdown.careline.models import Procedure
from drdown.users.models import Patient


class TestModelProcedure(TestCase):
    """
        Test if model Procedure is working
    """

    def setUp(self):
        """
            Runs before every test
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

    def test_procedure_created_checkitens_only_on_first_run(self):
        """
            Test if a procedure created by a checklist have only the defined
            checkitens. It shouldn't have the amount changed after a second
            save.
        """

        self.checklist = self.patient1.checklist

        self.assertEquals(
            hasattr(self.patient1, 'checklist'),
            True
        )

        self.assertEquals(
            hasattr(self.patient1.checklist, 'procedure_set'),
            True
        )

        for procedure in self.checklist.procedure_set.all():
            self.assertEquals(
                procedure.checkitem_set.all().count(),
                len(Procedure.AGES)
            )

        # if we save the checklist again, the aumont of checkitens should
        # remain the same

        self.checklist.save()

        for procedure in self.checklist.procedure_set.all():
            self.assertEquals(
                procedure.checkitem_set.all().count(),
                len(Procedure.AGES)
            )
