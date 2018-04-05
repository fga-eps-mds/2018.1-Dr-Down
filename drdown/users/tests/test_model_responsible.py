from test_plus.test import TestCase

from ..models import Responsible, Patient


class TestModelResponsible(TestCase):

    def setUp(self):
        self.user_1 = self.make_user()
        self.user_2 = self.make_user(username="teste_2")
        self.patient = Patient.objects.create(ses="1234567", user=self.user_2, priority=1)
        self.responsible = Responsible.objects.create(cpf="974.220.200-16", patient=self.patient, user=self.user_1)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user_1.get_absolute_url(),
            '/users/testuser/'
        )

    def test_one_to_one_relation(self):
        self.assertIs(self.user_1, self.responsible.user)
        self.assertIs(self.responsible, self.user_1.responsible)

    def test_delete_cascade(self):

        self.assertEquals(Responsible.objects.get(cpf="974.220.200-16"), self.responsible)

        self.user_1.delete()

        with self.assertRaises(Responsible.DoesNotExist):
            Responsible.objects.get(cpf="974.220.200-16")
