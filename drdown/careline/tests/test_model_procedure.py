from test_plus.test import TestCase

from drdown.careline.models import Procedure, Checklist
from drdown.users.models import Patient



class TestModelProcedureNoSetUp(TestCase):
    """
        Test if model Procedure is working (No setUp method)
    """

    def test_convert_age_to_item(self):

        test_cases = [
            (19, Procedure.AGE_SIX_TO_TEN_YEARS),
            (0, Procedure.AGE_NEWBORN),
            (-1, Procedure.AGE_NEWBORN),
            (0.4, Procedure.AGE_NEWBORN),
            (0.5, Procedure.AGE_SIX_MONTHS),
            (0.6, Procedure.AGE_SIX_MONTHS),
            (0.9, Procedure.AGE_SIX_MONTHS),
            (1, Procedure.AGE_ONE_YEAR),
            (2, Procedure.AGE_TWO_YEARS),
            (3, Procedure.AGE_THREE_YEARS),
            (4, Procedure.AGE_THREE_YEARS),
            (5, Procedure.AGE_FIVE_YEARS),
            (6, Procedure.AGE_SIX_TO_TEN_YEARS),
            (7, Procedure.AGE_SIX_TO_TEN_YEARS),
            (8, Procedure.AGE_SIX_TO_TEN_YEARS),
            (9, Procedure.AGE_SIX_TO_TEN_YEARS),
            (10, Procedure.AGE_SIX_TO_TEN_YEARS),
            (11, Procedure.AGE_SIX_TO_TEN_YEARS),
        ]

        for i in test_cases:
            self.assertEquals(
                Procedure.convert_age_to_item(i[0]),
                i[1]
            )

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
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible=None
        )

    def test_get_checkitens_ordered(self):
        """
            Test if the method returns a list ordered in the rigth order
        """

        procedures = list(self.patient1.checklist.procedure_set.all())
        chosen_procedure = procedures.pop(0)

        ordered = chosen_procedure.get_checkitens_ordered()

        for i in range(0, Procedure.AGES.__len__()):
            self.assertEquals(
                next(ordered).age,
                Procedure.AGES[i]
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

        # if we save the checklist again (and force execution of create_checkitens on procedures), the aumont
        # of checkitens should remain the same

        self.checklist.save()

        for procedure in self.checklist.procedure_set.all():

            # any combination of ages needed and required will serve us
            procedure.create_check_items(ages_needed=Procedure.AGES, ages_required=[])

            self.assertEquals(
                procedure.checkitem_set.all().count(),
                len(Procedure.AGES)
            )
