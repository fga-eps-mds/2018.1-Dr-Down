
from test_plus.test import TestCase
from django.contrib.auth.models import Group


from ..models.model_doctor import Doctor


class TestModelDoctor(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.doctor = Doctor.objects.create(
            cpf="057.641.271-65", user=self.user, speciality=Doctor.NEUROLOGY)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_one_to_one_relation(self):
        self.assertIs(self.user, self.doctor.user)
        self.assertIs(self.doctor, self.user.doctor)

    def test_delete_cascade(self):

        self.assertEquals(Doctor.objects.get(
            cpf="057.641.271-65"), self.doctor)

        self.user.delete()

        with self.assertRaises(Doctor.DoesNotExist):
            Doctor.objects.get(cpf="057.641.271-65")


class TestModelDoctorNoSetUp(TestCase):

    def test_save_making_changes_on_user(self):

        # this test should have no setup executed before it

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
        self.assertEquals(self.user.is_staff, True)
        self.assertEqual(self.user.groups.get(
            name=Doctor.GROUP_NAME), doctor_group)
