from test_plus.test import TestCase
from django.contrib.auth.models import Group, Permission, ContentType
from ..admin import EmployeeAdmin
from ..models import Employee, Patient, Responsible
from ..models.model_employee import set_permissions


class TestModelEmployee(TestCase):
    """
    Test if model Employee is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user = self.make_user()
        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user,
            departament=Employee.NEUROLOGY
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

        self.assertIs(self.user, self.employee.user)
        self.assertIs(self.employee, self.user.employee)

    def test_delete_cascade(self):
        """
        This test check if all object data is deleted along with it.
        """

        self.assertEquals(
            Employee.objects.get(cpf="974.220.200-16"),
            self.employee
        )

        self.user.delete()

        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(cpf="974.220.200-16")

    def test__str__(self):
        """
        This test check if __str__ is returning the data correctly.
        """

        self.assertEqual(
            self.employee.__str__(),
            (
                self.user.get_username() +
                " - " +
                self.employee.get_departament_display()
            )
        )


class TestModelEmployeeNoSetUp(TestCase):

    def test_save_making_changes_on_user(self):
        """
        This test should have no setup executed before it
        """

        self.user = self.make_user()

        self.assertEquals(self.user.is_staff, False)

        with self.assertRaises(Group.DoesNotExist):
            self.user.groups.get(name=Employee.GROUP_NAME)

        # now we add the employee<--->user relation
        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user,
            departament=Employee.NEUROLOGY
        )

        # it should create the group with permissons
        employee_group = Group.objects.get(name=Employee.GROUP_NAME)

        mock_group = Group.objects.create(name="mock")

        set_permissions(
            Patient,
            mock_group,
            change=True,
            add=True
        )

        set_permissions(
            Responsible,
            mock_group,
            change=True,
            add=True
        )

        self.assertQuerysetEqual(
            employee_group.permissions.all(),
            mock_group.permissions.all(),
            transform=lambda x: x
        )

        # and change things in the user
        self.assertEquals(self.user.is_staff, True)

        self.assertEqual(
            self.user.groups.get(name=Employee.GROUP_NAME),
            employee_group
        )

    def test_permission_set(self):

        # this will be tested with the Patient model
        content_type = ContentType.objects.get_for_model(Patient)

        mock_group = Group.objects.create(name="mock")

        # adds all permissions avaliable in set_permissions
        set_permissions(
            Patient,
            mock_group,
            change=True,
            add=True,
            delete=True
        )

        # check if the where added
        self.assertQuerysetEqual(
            Permission.objects.filter(content_type=content_type),
            mock_group.permissions.all(),
            transform=lambda x: x
        )

    def test_readonly_user(self):
        """
        Test is user field is read_only after creation of an employee
        """

        self.user = self.make_user()

        ma = EmployeeAdmin(model=Employee, admin_site=None)

        self.assertEqual(
            hasattr(self.user, 'employee'),
            False
        )
        # since there is no atribute employee in self user, we
        # can assume that obj=None
        self.assertEqual(
            list(ma.get_readonly_fields(self, obj=None)),
            []
        )

        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user,
            departament=Employee.NEUROLOGY
        )

        self.assertEqual(
            hasattr(self.user, 'employee'),
            True
        )

        ma1 = EmployeeAdmin(model=Employee, admin_site=None)
        self.assertEqual(
            list(ma1.get_readonly_fields(self, obj=self.user.employee)),
            ['user']
        )
