from test_plus.test import TestCase
from django.test import RequestFactory
from django.test.client import Client


from ..models import Employee


class TestViewEmployee (TestCase):
    """
    Test if View Employee is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.client = Client()
        self.user = self.make_user()
        self.employee = Employee.objects.create(cpf="974.220.200-16", user=self.user, departament=Employee.ADMINISTRATION)

    def test_employee_get_context_data(self):
        """
        Makes sure that the employee data is showing at the user detail view
        """

        self.employee.save()
        self.client.force_login(user=self.user)

        response = self.client.get(path='/users/testuser/', follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(self.user.employee.cpf, self.employee.cpf)

        self.assertContains(response, text=self.user.username)
        self.assertContains(response, text=self.user.username)

        self.assertContains(response, text=self.user.employee.cpf)
