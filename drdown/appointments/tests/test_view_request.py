from test_plus.test import TestCase
from ..models.model_appointment import Appointment
from ..models.model_request import AppointmentRequest
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from drdown.users.models.model_patient import Patient
from django.urls import reverse


class TestViewRequest(TestCase):

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

        self.request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.SPEECH_THERAPHY,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )

    def test_request_list_view_patient(self):
        """
        Makes sure that the request list view is loaded correctly
        """
        self.client.force_login(user=self.user)
        response = self.client.get(
            path=reverse(
                viewname='appointments:list_requests'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_request_list_view_doctor(self):
        """
        Makes sure that the request list view is loaded correctly
        """
        self.client.force_login(user=self.user2)
        response = self.client.get(
            path=reverse(
                viewname='appointments:list_requests'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_request_list_view_employee(self):
        """
        Makes sure that the request list view is loaded correctly
        """
        self.client.force_login(user=self.user3)
        response = self.client.get(
            path=reverse(
                viewname='appointments:list_requests'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_request_list_view_responsible(self):
        """
        Makes sure that the request list view is loaded correctly
        """
        self.client.force_login(user=self.user4)
        response = self.client.get(
            path=reverse(
                viewname='appointments:list_requests'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_request_create_view(self):
        """
        Makes sure that the request create view is loaded correctly
        """
        self.client.force_login(user=self.user)
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request'
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_request_update_view(self):
        """
        Makes sure that the request update view is loaded correctly
        """
        self.client.force_login(user=self.user)
        response = self.client.get(
            path=reverse(
                viewname='appointments:update_request',
                args=(self.request.pk,)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_request_update_status_view_form_valid(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user3)
        data = {
            'observation': 'Some motive'
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:update_status_request',
                args=(self.request.pk,),
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

