from test_plus.test import TestCase
from ..models.model_appointment import Appointment
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.utils.translation import ugettext_lazy as _


class TestModelAppointment(TestCase):

    def setUp(self):
        """
            This method will run before any test case.
        """

        self.user = self.make_user(username='user_1')
        self.user2 = self.make_user(username='user_2')
        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user,
            priority=1,
            mother_name="Mother",
            father_name="Father",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911"
        )

        self.doctor = HealthTeam.objects.create(
            cpf="057.641.271-65",
            user=self.user2,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.appointment = Appointment.objects.create(
            date="2040-08-10",
            time="15:45",
            speciality=Appointment.SPEECH_THERAPHY,
            doctor=self.doctor,
            patient=self.patient,
            status=Appointment.SCHEDULED
        )

    def test_one_to_one_relation(self):
        """
            Test to verify if the relations work
        """

        self.assertIs(self.patient, self.appointment.patient)
        self.assertIs(self.doctor, self.appointment.doctor)

    def test_delete_cascade_patient(self):
        """
            Verify delete the relation objects
        """

        self.patient.delete()
        with self.assertRaises(Appointment.DoesNotExist):
            Appointment.objects.get()

    def test_delete_cascade_doctor(self):
        """
            Verify delete the relation objects
        """

        self.doctor.delete()
        with self.assertRaises(Appointment.DoesNotExist):
            Appointment.objects.get()

    def test_save_date_ok(self):
        """
        Test to verify if date is correctly passed
        """

        self.assertEquals(self.appointment.date, '2040-08-10')

    def test_save_time_ok(self):
        """
        Test to verify if time is correctly passed
        """

        self.assertEquals(self.appointment.time, "15:45")

    def test_save_patient_ok(self):
        """
        Test to verify if patient is correctly passed
        """

        self.assertEquals(self.appointment.patient, self.patient)

    def test_save_doctor_ok(self):
        """
        Test to verify if doctor is correctly passed
        """

        self.assertEquals(self.appointment.doctor, self.doctor)

    def test_save_status_ok(self):
        """
        Test to verify if status is correctly passed
        """

        self.assertEquals(self.appointment.status, Appointment.SCHEDULED)

    def test_save_speciality_ok(self):
        """
        Test to verify if speciality is correctly passed
        """

        self.assertEquals(
            self.appointment.speciality,
            Appointment.SPEECH_THERAPHY
        )

    def test_str_is_equal_to_title(self):
        """
        Test if method `__str__` is returning "Appointment of <patient>"
        """
        self.user.name = 'User'
        self.assertEqual(
            str(self.appointment),
            _('Appointment of ') + self.patient.user.name
        )
