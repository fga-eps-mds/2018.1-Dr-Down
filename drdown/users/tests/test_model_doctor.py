from test_plus.test import TestCase
from ..admin import DoctorAdmin
from django.contrib.auth.models import Group


from ..models.model_doctor import Doctor
from ..models import User


class TestModelDoctor(TestCase):
    """
    Test if model Doctor is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user = self.make_user()
        self.doctor = Doctor.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=Doctor.NEUROLOGY)

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

        self.assertIs(self.user, self.doctor.user)
        self.assertIs(self.doctor, self.user.doctor)

    def test_delete_cascade(self):
        """
        This test check if all object data is deleted along with it.
        """

        self.assertEquals(Doctor.objects.get(
            cpf="057.641.271-65"), self.doctor)

        self.user.delete()

        with self.assertRaises(Doctor.DoesNotExist):
            Doctor.objects.get(cpf="057.641.271-65")

    def test__str__(self):
        """
        This test check if __str__ is returning the data correctly.
        """
        self.assertEqual(
            self.doctor.__str__(),
            (
                self.user.get_username() +
                " - " +
                self.doctor.get_speciality_display()
            )
        )


class TestModelDoctorNoSetUp(TestCase):

    def test_save_making_changes_on_user(self):
        """
        This test should have no setup executed before it.
        """

        self.user = self.make_user()

        self.assertEquals(self.user.is_staff, False)

        with self.assertRaises(Group.DoesNotExist):
            self.user.groups.get(name=Doctor.GROUP_NAME)

        # now we add the doctor<--->user relation
        self.doctor = Doctor.objects.create(
            cpf="057.641.271-65", user=self.user, speciality=Doctor.NEUROLOGY)

        # it should create the group
        doctor_group = Group.objects.get(name=Doctor.GROUP_NAME)

        # and change things in the user
        self.assertEqual(self.user.groups.get(
            name=Doctor.GROUP_NAME), doctor_group)


class ModelTestCase(TestCase):

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user1 = User.objects.create(
            name='Pedro',
            username='pedro',
            email='pedro@gmail.com',
            password='pedro123456'
        )

        self.doctor1 = Doctor.objects.create(
            cpf='057.640.991-02',
            crm='1234567',
            speciality=Doctor.PEDIATRICS,
            user=self.user1
        )

    def test_save_cpf_ok(self):
        """
        This method will check if the cpf is equal to the informed
        """

        self.assertEquals(self.doctor1.cpf, '057.640.991-02')

    def test_save_crm_ok(self):
        """
        This method will check if the crm is equal to the informed
        """
        self.assertEquals(self.doctor1.crm, '1234567')

    def test_save_speciality_ok(self):
        """
        This method will check if the speciality is equal to the informed
        """
        self.assertEquals(self.doctor1.speciality, Doctor.PEDIATRICS)

    def test_save_cpf_error(self):
        """
        This method will check if the cpf is different from informed
        """

        self.assertNotEquals(self.doctor1.cpf, '057.641.271-65')

    def test_save_crm_error(self):
        """
        This method will check if the crm is different from informed
        """

        self.assertNotEquals(self.doctor1.crm, '7654321')

    def test_save_speciality_error(self):
        """
        This method will check if the speciality is different from informed
        """

        self.assertNotEquals(self.doctor1.speciality, Doctor.CARDIOLOGY)

    def teste_readonly_user(self):

        self.user = self.make_user()

        ma = DoctorAdmin(model=Doctor, admin_site=None)

        self.assertEqual(
            hasattr(self.user, 'doctor'),
            False
        )
        # since there is no atribute patient in self user, we
        # can assume that obj=None
        self.assertEqual(
            list(ma.get_readonly_fields(self, obj=None)),
            []
        )

        self.doctor = Doctor.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=Doctor.NEUROLOGY)

        self.assertEqual(
            hasattr(self.user, 'doctor'),
            True
        )

        ma1 = DoctorAdmin(model=Doctor, admin_site=None)
        self.assertEqual(
            list(ma1.get_readonly_fields(self, obj=self.user.doctor)),
            ['user']
        )
