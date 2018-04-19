from test_plus.test import TestCase
from ..admin import Health_TeamAdmin
from django.contrib.auth.models import Group


from ..models.model_health_team import Health_Team
from ..models import User


class TestModelHealth_Team(TestCase):
    """
    Test if model Health_Team is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user = self.make_user()
        self.health_team = Health_Team.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=Health_Team.NEUROLOGY)

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

        self.assertIs(self.user, self.health_team.user)
        self.assertIs(self.health_team, self.user.health_team)

    def test_delete_cascade(self):
        """
        This test check if all object data is deleted along with it.
        """

        self.assertEquals(Health_Team.objects.get(
            cpf="057.641.271-65"), self.health_team)

        self.user.delete()

        with self.assertRaises(Health_Team.DoesNotExist):
            Health_Team.objects.get(cpf="057.641.271-65")

    def test__str__(self):
        """
        This test check if __str__ is returning the data correctly.
        """
        self.assertEqual(
            self.health_team.__str__(),
            (
                self.user.get_username() +
                " - " +
                self.health_team.get_speciality_display()
            )
        )


class TestModelHealth_TeamNoSetUp(TestCase):

    def test_save_making_changes_on_user(self):
        """
        This test should have no setup executed before it.
        """

        self.user = self.make_user()

        self.assertEquals(self.user.is_staff, False)

        with self.assertRaises(Group.DoesNotExist):
            self.user.groups.get(name=Health_Team.GROUP_NAME)

        # now we add the health team <--->user relation
        self.health_team = Health_Team.objects.create(
            cpf="057.641.271-65", user=self.user, speciality=Health_Team.NEUROLOGY)

        # it should create the group
        health_team_group = Group.objects.get(name=Health_Team.GROUP_NAME)

        # and change things in the user
        self.assertEqual(self.user.groups.get(
            name=Health_Team.GROUP_NAME), health_team_group)


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

        self.health_team1 = Health_Team.objects.create(
            cpf='057.640.991-02',
            register_number='1234567',
            speciality=Health_Team.PEDIATRICS,
            user=self.user1
        )

    def test_save_cpf_ok(self):
        """
        This method will check if the cpf is equal to the informed
        """

        self.assertEquals(self.health_team1.cpf, '057.640.991-02')

    def test_save_crm_ok(self):
        """
        This method will check if the crm is equal to the informed
        """
        self.assertEquals(self.health_team1.register_number, '1234567')

    def test_save_speciality_ok(self):
        """
        This method will check if the speciality is equal to the informed
        """
        self.assertEquals(self.health_team1.speciality, Health_Team.PEDIATRICS)

    def test_save_cpf_error(self):
        """
        This method will check if the cpf is different from informed
        """

        self.assertNotEquals(self.health_team1.cpf, '057.641.271-65')

    def test_save_crm_error(self):
        """
        This method will check if the crm is different from informed
        """

        self.assertNotEquals(self.health_team1.register_number, '7654321')

    def test_save_speciality_error(self):
        """
        This method will check if the speciality is different from informed
        """

        self.assertNotEquals(self.health_team1.speciality, Health_Team.CARDIOLOGY)

    def test_readonly_user(self):
        """
        Test is user field is read_only after creation of an health team
        """

        self.user = self.make_user()

        ma = Health_TeamAdmin(model=Health_Team, admin_site=None)

        self.assertEqual(
            hasattr(self.user, 'health_team'),
            False
        )
        # since there is no atribute patient in self user, we
        # can assume that obj=None
        self.assertEqual(
            list(ma.get_readonly_fields(self, obj=None)),
            []
        )

        self.health_team = Health_Team.objects.create(
            cpf="057.641.271-65",
            user=self.user,
            speciality=Health_Team.NEUROLOGY)

        self.assertEqual(
            hasattr(self.user, 'health_team'),
            True
        )

        ma1 = Health_TeamAdmin(model=Health_Team, admin_site=None)
        self.assertEqual(
            list(ma1.get_readonly_fields(self, obj=self.user.health_team)),
            ['user']
        )
