from test_plus.test import TestCase
from django.test.client import Client
from ..models.model_curves import Curves
from drdown.users.models.model_patient import Patient


class TestModelCurves(TestCase):

    WEIGHT = 10
    HEIGHT = 123
    CEPHALIC_PERIMETER = 30
    AGE = 1

    def setUp(self):
        """
        This method will run before any test case.
        """

        self.client = Client()

        self.user = self.make_user()

        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
        )

        self.curve = Curves.objects.create(
            patient=self.patient,
            weight=self.WEIGHT,
            height=self.HEIGHT,
            cephalic_perimeter=self.CEPHALIC_PERIMETER,
            age=self.AGE,
        )

    def test_get_bmi(self):
        """
        Test if BMI is calculates correctly
        """
        bmi = self.WEIGHT / (self.HEIGHT/100 * self.HEIGHT/100)

        self.assertAlmostEqual(bmi, self.curve.get_bmi())
