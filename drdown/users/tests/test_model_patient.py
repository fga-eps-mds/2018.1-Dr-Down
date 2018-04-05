from test_plus.test import TestCase

from ..models import Patient


class TestModelPatient(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.patient = Patient.objects.create(ses="1234567", user=self.user, priority=1)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_one_to_one_relation(self):
        self.assertIs(self.user, self.patient.user)
        self.assertIs(self.patient, self.user.patient)

    def test_delete_cascade(self):

        self.assertEquals(Patient.objects.get(ses="1234567"), self.patient)

        self.user.delete()

        with self.assertRaises(Patient.DoesNotExist):
            Patient.objects.get(ses="1234567")
