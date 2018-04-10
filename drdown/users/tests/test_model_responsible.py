from test_plus.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Responsible, Patient


class TestModelResponsible(TestCase):

    def setUp(self):
        self.user_1 = self.make_user()
        self.user_2 = self.make_user(username="teste_2")
        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user_2,
            priority=1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911"
        )

        self.responsible = Responsible.objects.create(
            cpf="974.220.200-16",
            patient=self.patient,
            user=self.user_1
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user_1.get_absolute_url(),
            '/users/testuser/'
        )

    def test__str__(self):
        self.assertEqual(
            self.responsible.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_one_to_one_relation(self):
        self.assertIs(self.user_1, self.responsible.user)
        self.assertIs(self.responsible, self.user_1.responsible)

    def test_delete_cascade(self):

        self.assertEquals(
            Responsible.objects.get(cpf="974.220.200-16"),
            self.responsible
        )

        self.user_1.delete()

        with self.assertRaises(Responsible.DoesNotExist):
            Responsible.objects.get(cpf="974.220.200-16")

    def test_patient_responsible_for_itself(self):

        # user 2 is the patient
        # we will check if its not possible to set
        # a patient as its responsible

        self.assertIs(self.patient.user, self.user_2)

        with self.assertRaises(ValidationError):
            res = Responsible.objects.create(
                cpf="680.178.880-90",
                patient=self.patient,
                user=self.user_2
            )
