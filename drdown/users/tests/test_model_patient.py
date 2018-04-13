from test_plus.test import TestCase

from ..models import Patient


class TestModelPatient(TestCase):
    """
    Test if model Patient is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user = self.make_user()
        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user,
            priority=1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911"
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
