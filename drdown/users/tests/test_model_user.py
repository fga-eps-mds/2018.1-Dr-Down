from test_plus.test import TestCase
from drdown.users.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date

from ..models import Employee, HealthTeam, Patient, Responsible


class TestUser(TestCase):
    """
    Test if model Employee is working correctly
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.user = self.make_user()

    def test__str__(self):
        """
        This test check if __str__ is returning the data correctly.
        """

        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        """
        This test will get the absolute url of user.
        """

        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_short_name(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.user.get_short_name(),
                          self.user.first_name)

    def test_age(self):
        """
        Test to get age of user
        """

        test_ages = [
            5, 10, 4, 66, 12
        ]

        today = timezone.localdate()

        for test_age in test_ages:
            self.user.birthday = timezone.datetime(
                year=(today.year - test_age),
                month=today.month,
                day=today.day
            )

            self.user.save()
            self.user.refresh_from_db()

            self.assertEquals(
                self.user.age(),
                test_age
            )

        edge_cases_months = [
            -1,
            0,
            1,
            5,
            6,
            7,
            8,
            10,
            11,
            12,
            13
        ]

        for months in edge_cases_months:
            self.user.birthday = today + relativedelta(months=-months)

            self.user.save()
            self.user.refresh_from_db()

            if 6 <= months < 12:
                self.assertEquals(
                    self.user.age(),
                    0.5
                )
            elif months < 6:
                if months is 6:
                    self.assertEquals(
                        self.user.age(),
                        0
                    )
            elif months >= 12:
                if months is 6:
                    self.assertGreaterEqual(
                        self.user.age(),
                        1
                    )

    def test_invalid_birthday(self):
        today = timezone.localdate()
        tomorrow = today + relativedelta(days=1)
        past = date(1800, 1, 1)

        with self.assertRaises(ValidationError):
            self.user.birthday = tomorrow
            self.user.save()
            self.user.clean()

        with self.assertRaises(ValidationError):
            self.user.birthday = past
            self.user.save()
            self.user.clean()


class TestField(TestCase):

    def setUp(self):
        """
        This method will run before any test.
        """

        self.superuser = User.objects.create_superuser(
            name='Ohaio',
            last_name='Nini',
            first_name='Ohaio',
            username='Ohaionini',
            email='ohaio@gmail.com',
            password='ohaio123456',
            birthday='1998-03-05',
            telephone='(11)11111-1111',
            gender='M',
            created_at='2018-03-05',
            updated_at='2018-03-05',
            photo='example.jpg'
        )

        self.user1 = User.objects.create_user(
            first_name='Pedro',
            last_name='Victor',
            name='Pedro',
            username='pedro100',
            email='pedro@gmail.com',
            password='pedro123456',
            birthday='1998-04-05',
            telephone='(22)22222-2222',
            gender='F',
            created_at='2018-04-05',
            updated_at='2018-04-05',
            photo='example.jpg'
        )

        self.user2 = User.objects.create_user(
            first_name='Jobs',
            last_name='Rogers',
            name='Jobs',
            username='jobs101',
            email='jobs@gmail.com',
            password='jobs123456',
            birthday='1998-05-05',
            telephone='(33)33333-3333',
            gender='M',
            created_at='2018-05-05',
            updated_at='2018-05-05',
            photo='example.jpg'
        )

    def tearDown(self):
        """
        This method will run after any test.
        """

        self.superuser.delete()
        self.user1.delete()
        self.user2.delete()

    def test_short_name(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.superuser.get_short_name(), self.superuser.name)
        self.assertEquals(self.user1.get_short_name(), self.user1.name)
        self.assertEquals(self.user2.get_short_name(), self.user2.name)

    def test_name(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.superuser.name, 'Ohaio')
        self.assertEquals(self.user1.name, 'Pedro')
        self.assertEquals(self.user2.name, 'Jobs')

    def test_username(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.superuser.username, 'Ohaionini')
        self.assertEquals(self.user1.username, 'pedro100')
        self.assertEquals(self.user2.username, 'jobs101')

    def test_invalid_name(self):
        """
        Test to get the full name of user
        """

        self.assertNotEquals(self.superuser.name, '')
        self.assertNotEquals(self.user1.name, '')
        self.assertNotEquals(self.user2.name, '')

    def test_first_name(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.superuser.first_name, 'Ohaio')
        self.assertEquals(self.user1.first_name, 'Pedro')
        self.assertEquals(self.user2.first_name, 'Jobs')

    def test_invalid_first_name(self):
        """
        Test to get the full name of user
        """

        self.assertNotEquals(self.superuser.first_name, '')
        self.assertNotEquals(self.user1.first_name, '')
        self.assertNotEquals(self.user2.first_name, '')

    def test_last_name(self):
        """
        Test to get the full name of user
        """

        self.assertEquals(self.superuser.last_name, 'Nini')
        self.assertEquals(self.user1.last_name, 'Victor')
        self.assertEquals(self.user2.last_name, 'Rogers')

    def test_invalid_last_name(self):
        """
        Test to get the full name of user
        """

        self.assertNotEquals(self.superuser.last_name, '')
        self.assertNotEquals(self.user1.last_name, '')
        self.assertNotEquals(self.user2.last_name, '')

    def test_birthday(self):
        """
        Test for verify if the birthday is the same for compare
        """

        self.assertEquals(self.superuser.birthday, '1998-03-05')
        self.assertEquals(self.user1.birthday, '1998-04-05')
        self.assertEquals(self.user2.birthday, '1998-05-05')

    def test_in_not_birthday(self):
        """
        Test for verify if the birthday is the same for compare
        """

        self.assertNotEquals(self.superuser.birthday, '')
        self.assertNotEquals(self.user1.birthday, '')
        self.assertNotEquals(self.user2.birthday, '')

    def test_telephone(self):
        """
        Test for verify if the phone is the same for compare
        """

        self.assertEquals(self.superuser.telephone, '(11)11111-1111')
        self.assertEquals(self.user1.telephone, '(22)22222-2222')
        self.assertEquals(self.user2.telephone, '(33)33333-3333')

    def test_is_not_telephone(self):
        """
        Test for verify if the phone is the same for compare
        """

        self.assertNotEquals(self.superuser.telephone, '')
        self.assertNotEquals(self.user1.telephone, '')
        self.assertNotEquals(self.user2.telephone, '')

    def test_email(self):
        """
        Test for verify if the phone is the same for compare
        """

        self.assertEquals(self.superuser.email, 'ohaio@gmail.com')
        self.assertEquals(self.user1.email, 'pedro@gmail.com')
        self.assertEquals(self.user2.email, 'jobs@gmail.com')

    def test_is_not_email(self):
        """
        Test for verify if the phone is the diferent for compare
        """

        self.assertNotEqual(self.superuser.email, '')
        self.assertNotEqual(self.user1.email, '')
        self.assertNotEqual(self.user2.email, '')

    def test_gender(self):
        """
        Test for verify if the gender is the same of compare
        """

        self.assertEquals(self.superuser.gender, 'M')
        self.assertEquals(self.user1.gender, 'F')
        self.assertEquals(self.user2.gender, 'M')

    def test_created_at(self):
        """
        Test for verify if the create_at is the same for compare
        """

        self.assertEquals(self.superuser.created_at, '2018-03-05')
        self.assertEquals(self.user1.created_at, '2018-04-05')
        self.assertEquals(self.user2.created_at, '2018-05-05')

    def test_in_not_creted_at(self):
        """
        Test for verify if the create_at is diferent for compare
        """

        self.assertNotEquals(self.superuser.created_at, '')
        self.assertNotEquals(self.user1.created_at, '')
        self.assertNotEquals(self.user2.created_at, '')

    def test_updated_at(self):
        """
        Test for verify if the update_at is the same for compare
        """

        self.assertEquals(self.superuser.updated_at, '2018-03-05')
        self.assertEquals(self.user1.updated_at, '2018-04-05')
        self.assertEquals(self.user2.updated_at, '2018-05-05')

    def test_in_not_updated_at(self):
        """
        Test for verify if the update_at is the different for compare
        """

        self.assertNotEquals(self.superuser.updated_at, '')
        self.assertNotEquals(self.user1.updated_at, '')
        self.assertNotEquals(self.user2.updated_at, '')

    def test_photo(self):
        """
        Test for verifying if the photo is the same for compare
        """
        self.assertEquals(self.superuser.photo, 'example.jpg')
        self.assertEquals(self.user1.photo, 'example.jpg')
        self.assertEquals(self.user2.photo, 'example.jpg')

    def test_updated_at_photo(self):
        """
        Test for verifying if the update_at is different for compare
        """

        self.assertNotEquals(self.superuser.photo, '')
        self.assertNotEquals(self.user1.photo, '')
        self.assertNotEquals(self.user2.photo, '')

    def test_multiple_specialization(self):
        """
        Defining an initial relation to user
        """

        Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user1,
            departament=Employee.ADMINISTRATION
        )

        # try to define a new relation to the same user
        with(self.assertRaises(ValidationError)):
            Patient.objects.create(
                ses="1234567",
                user=self.user1,
                mother_name="Mãe",
                father_name="Pai",
                ethnicity=3,
                sus_number="12345678911",
                civil_registry_of_birth="12345678911",
                declaration_of_live_birth="12345678911"
            )

        with(self.assertRaises(ValidationError)):
            Responsible.objects.create(
                cpf="974.220.200-16",
                user=self.user1
            )

        with(self.assertRaises(ValidationError)):
            HealthTeam.objects.create(
                cpf="057.641.271-65",
                user=self.user1,
                speciality=HealthTeam.NEUROLOGY,
                council_acronym=HealthTeam.CRM,
                register_number="1234567",
                registration_state=HealthTeam.DF,
            )

        # test employee again
        with(self.assertRaises(ValidationError)):
            Employee.objects.create(
                cpf="057.641.271-65",
                user=self.user1,
                departament=Employee.ADMINISTRATION
            )

    def test_employee_specialization_on_delete_reset_flag(self):
        """
        Test that checks if the has_specialization flag
        returns to "false" when the user loses the
        employee specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        # define a initial relation to user
        employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user1,
            departament=Employee.ADMINISTRATION
        )

        self.assertEqual(self.user1.has_specialization, True)

        employee.delete()

        self.assertEqual(self.user1.has_specialization, False)

    def test_health_team_specialization_on_delete_reset_flag(self):
        """
        Test that checks if the has_specialization flag
        returns to "false" when the user loses the
        health team specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        # define a initial relation to user
        health_team = HealthTeam.objects.create(
            cpf="057.641.271-65",
            user=self.user1,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.assertEqual(self.user1.has_specialization, True)

        health_team.delete()

        self.assertEqual(self.user1.has_specialization, False)

    def test_responsible_specialization_on_delete_reset_flag(self):
        """
        Test that checks if the has_specialization flag
        returns to "false" when the user loses the
        responsible specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        # define a initial relation to user
        responsible = Responsible.objects.create(
            cpf="974.220.200-16",
            user=self.user1
        )

        self.assertEqual(self.user1.has_specialization, True)

        responsible.delete()

        self.assertEqual(self.user1.has_specialization, False)

    def test_patient_specialization_on_delete_reset_flag(self):
        """
        Test that checks if the has_specialization flag
        returns to "false" when the user loses the
        patient specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        # define a initial relation to user
        patient = Patient.objects.create(
            ses="1234567",
            user=self.user1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911"
        )

        self.assertEqual(self.user1.has_specialization, True)

        patient.delete()

        self.assertEqual(self.user1.has_specialization, False)

    def test_removing_employee_specialization_remove_staff(self):
        """
        Test that checks if the user loses staff
        status when he loses the employee specialization
        """

        self.assertEqual(self.user1.has_specialization, False)
        self.assertEqual(self.user1.is_staff, False)

        employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user1,
            departament=Employee.ADMINISTRATION
        )

        self.assertEqual(self.user1.has_specialization, True)
        self.assertEqual(self.user1.is_staff, True)

        employee.delete()

        self.assertEqual(self.user1.has_specialization, False)
        self.assertEqual(self.user1.is_staff, False)

    def test_removing_health_team_specialization_remove_staff(self):
        """
        Test that checks if the user loses staff
        status when he loses the health team specialization
        """

        self.assertEqual(self.user1.has_specialization, False)
        self.assertEqual(self.user1.is_staff, False)

        health_team = HealthTeam.objects.create(
                cpf="057.641.271-65",
                user=self.user1,
                speciality=HealthTeam.NEUROLOGY,
                council_acronym=HealthTeam.CRM,
                register_number="1234567",
                registration_state=HealthTeam.DF,
        )

        self.assertEqual(self.user1.has_specialization, True)
        self.assertEqual(self.user1.is_staff, True)

        health_team.delete()

        self.assertEqual(self.user1.has_specialization, False)
        self.assertEqual(self.user1.is_staff, False)

    def test_cant_update_user_on_responsible_specialization(self):
        """
        Test that verifies that the user field can not be updated in an responsible specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        responsible = Responsible.objects.create(
            cpf="507.522.730-94",
            user=self.user1,
        )

        self.assertEqual(self.user1.has_specialization, True)
        self.assertEqual(hasattr(self.user1, 'responsible'), True)

        with self.assertRaises(ValidationError):
            responsible.user = self.user2
            responsible.save()

    def test_cant_update_user_on_health_team_specialization(self):
        """
        Test that verifies that the user field can not be updated in an health team specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        health_team = HealthTeam.objects.create(
            cpf="507.522.730-94",
            user=self.user1,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.assertEqual(self.user1.has_specialization, True)
        self.assertEqual(hasattr(self.user1, 'healthteam'), True)

        with self.assertRaises(ValidationError):
            health_team.user = self.user2
            health_team.save()

    def test_cant_update_user_on_patient_specialization(self):
        """
        Test that verifies that the user field can not be updated in an patient specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        patient = Patient.objects.create(
            ses="1234567",
            user=self.user1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911"
        )

        self.assertEqual(self.user1.has_specialization, True)
        self.assertEqual(hasattr(self.user1, 'patient'), True)

        with self.assertRaises(ValidationError):
            patient.user = self.user2
            patient.save()

    def test_cant_update_user_on_employee_specialization(self):
        """
        Test that verifies that the user field can not be updated in an responsible specialization
        """

        self.assertEqual(self.user1.has_specialization, False)

        employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user1,
            departament=Employee.ADMINISTRATION
        )

        self.assertEqual(self.user1.has_specialization, True)
        self.assertEqual(hasattr(self.user1, 'employee'), True)

        with self.assertRaises(ValidationError):
            employee.user = self.user2
            employee.save()

    def test_delete_employee_specialization(self):
        """
        Test that checks if the bool has_specialization goes true when
        an employee is created and if that bool returns to false in the
        employee deletion
        """

        self.assertEqual(self.user1.has_specialization, False)

        employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user1,
            departament=Employee.ADMINISTRATION
        )

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'employee'), True)
        self.assertEqual(self.user1.has_specialization, True)

        employee.delete()
        self.assertEqual(self.user1.has_specialization, False)

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'employee'), False)
        self.assertEqual(self.user1.has_specialization, False)

    def test_delete_patient_specialization(self):
        """
        Test that checks if the bool has_specialization goes true when
        an patient is created and if that bool returns to false in the
        patient deletion
        """

        self.assertEqual(self.user1.has_specialization, False)

        patient = Patient.objects.create(
            ses="1234567",
            user=self.user1,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911"
        )
        self.assertEqual(hasattr(self.user1, 'patient'), True)
        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'patient'), True)
        self.assertEqual(self.user1.has_specialization, True)

        patient.delete()
        self.assertEqual(self.user1.has_specialization, False)

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'patient'), False)
        self.assertEqual(self.user1.has_specialization, False)

    def test_delete_responsible_specialization(self):
        """
        Test that checks if the bool has_specialization goes true when
        an responsible is created and if that bool returns to false in the
        responsible deletion
        """

        self.assertEqual(self.user1.has_specialization, False)

        responsible = Responsible.objects.create(
            cpf="974.220.200-16",
            user=self.user1,
        )

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'responsible'), True)
        self.assertEqual(self.user1.has_specialization, True)

        responsible.delete()
        self.assertEqual(self.user1.has_specialization, False)

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'responsible'), False)
        self.assertEqual(self.user1.has_specialization, False)

    def test_delete_health_team_specialization(self):
        """
        Test that checks if the bool has_specialization goes true when
        an health team is created and if that bool returns to false in the
        health team deletion
        """

        self.assertEqual(self.user1.has_specialization, False)

        health_team = HealthTeam.objects.create(
            cpf="507.522.730-94",
            user=self.user1,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'healthteam'), True)
        self.assertEqual(self.user1.has_specialization, True)

        health_team.delete()
        self.assertEqual(self.user1.has_specialization, False)

        self.user1.refresh_from_db()

        self.assertEqual(hasattr(self.user1, 'healthteam'), False)
        self.assertEqual(self.user1.has_specialization, False)
