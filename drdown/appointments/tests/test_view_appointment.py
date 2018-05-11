from test_plus.test import TestCase
from ..models.model_appointment import Appointment
from ..models.model_request import AppointmentRequest
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from drdown.users.models.model_patient import Patient
from django.urls import reverse


class TestViewAppointment(TestCase):

    def setUp(self):
        """
        This method will run before any test case.
        """
        self.user = self.make_user(username='user_1')
        self.user2 = self.make_user(username='user_2')
        self.user3 = self.make_user(username='user_3')
        self.user4 = self.make_user(username='user_4')
        self.user5 = self.make_user(username='user_5')

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

        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user3,
            departament=Employee.ADMINISTRATION
        )

        self.responsible = Responsible.objects.create(
            user=self.user4,
            cpf="022.852.870-46",
            patient=self.patient
        )

        self.appointment = Appointment.objects.create(
            date="2040-08-10",
            time="15:45",
            speciality=Appointment.SPEECH_THERAPHY,
            doctor=self.doctor,
            patient=self.patient,
            status=Appointment.SCHEDULED
        )

        self.client.force_login(user=self.user)

    def test_appointment_list_view(self):
        """
        Makes sure that the appointment list view is loaded correctly
        """

        response = self.client.get(
            path=reverse(
                viewname='appointments:list_appointments'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_appointment_create_view(self):
        """
        Makes sure that the appointment create view is loaded correctly
        """
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_appointment'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_appointment_update_view(self):
        """
        Makes sure that the appointment update view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='appointments:update_appointment',
                args=(self.appointment.pk,)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_post_cancel_view(self):
        """
        Makes sure that the appointment update status is loaded correctly
        """
        response = self.client.get(
            path=reverse(
            viewname='appointments:update_status_appointment',
            args=(self.appointment.pk,)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_appointment_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.SPEECH_THERAPHY,
            'doctor': self.doctor.pk,
            'patient': self.patient.pk,
            'date': '2050-05-12',
            'time': '20:00',
        }
        response = self.client.post(
            path=reverse('appointments:create_appointment'),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_appointment_form_valid_update_view(self):
        """
        Test if update form is valid with all required fields
        """
        self.client.force_login(user=self.user)
        data = {
            'speciality': Appointment.SPEECH_THERAPHY,
            'doctor': self.doctor.pk,
            'patient': self.patient.pk,
            'date': '2050-05-12',
            'time': '20:00',
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:update_appointment',
                args=(self.appointment.pk,)
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_delete_ok(self):
        """
        Test the page url status code.
        """

        self.client.force_login(user=self.user)
        data = {
            'speciality': Appointment.SPEECH_THERAPHY,
            'doctor': self.doctor.pk,
            'patient': self.patient.pk,
            'date': '2050-05-12',
            'time': '20:00',
        }

        response = self.client.post(
            path=reverse(
                viewname='appointments:update_status_appointment',
                args=(self.appointment.pk,)
            ),
            data=data,
            follow=True
        )
        self.assertEquals(response.status_code, 200)

    def test_list_view_appointments_patient(self):
        self.client.force_login(user=self.user)

        response = self.client.get(
            path=reverse(
                viewname='appointments:archive_month',
                args=('2040', '08'),
                )
            )
        self.assertEquals(response.status_code, 200)

    def test_list_view_appointments_health_team(self):
        self.client.force_login(user=self.user2)

        response = self.client.get(
            path=reverse(
                viewname='appointments:archive_month',
                args=('2040', '08'),
                )
            )
        self.assertEquals(response.status_code, 200)

    def test_list_view_appointments_employee(self):
        self.client.force_login(user=self.user3)

        response = self.client.get(
            path=reverse(
                viewname='appointments:archive_month',
                args=('2040', '08'),
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_list_view_appointments_responsible(self):
        self.responsible.save()
        self.client.force_login(user=self.user4)

        response = self.client.get(
            path=reverse(
                viewname='appointments:archive_month',
                args=('2040', '08'),
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_list_view_appointments(self):
        self.responsible.save()
        self.client.force_login(user=self.user5)

        response = self.client.get(
            path=reverse(
                viewname='appointments:archive_month',
                args=('2040', '08'),
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_appointment_from_request_context_data_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.SPEECH_THERAPHY,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        response = self.client.get(
            path=reverse(
                viewname='appointments:create_from_request',
                args=(request.pk,),
            ),
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, text=request.speciality)
        self.assertContains(response, text=request.shift)
        self.assertContains(response, text=request.get_day_display())

    def test_appointment_from_request_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.SPEECH_THERAPHY,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.SPEECH_THERAPHY,
            'doctor': self.doctor.pk,
            'patient': self.patient.pk,
            'date': '2050-05-12',
            'time': '20:00',
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_from_request',
                args=(request.pk,),
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

