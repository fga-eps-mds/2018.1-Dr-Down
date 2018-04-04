from test_plus.test import TestCase

from ..models import Employee


class TestModelEmployee(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.employee = Employee(cpf="974.220.200-16", user=self.user, departament=Employee.NEUROLOGY)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_one_to_one_relation(self):
        self.assertIs(self.user, self.employee.user)
        self.assertIs(self.employee, self.user.employee)

    def test_save_making_changes_on_user(self):
        self.employee.save()
        self.assertEquals(self.user.is_staff, True)
