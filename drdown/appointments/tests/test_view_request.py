from test_plus.test import TestCase
from ..models.model_appointment import Appointment
from ..models.model_request import AppointmentRequest
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from drdown.users.models.model_patient import Patient
from django.urls import reverse
from django.test.client import Client


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
        self.user6 = self.make_user(username='user_6')
        self.user7 = self.make_user(username='user_7')
        self.user8 = self.make_user(username='user_8')
        self.user9 = self.make_user(username='user_9')
        self.user10 = self.make_user(username='user_10')
        self.user11 = self.make_user(username='user_11')
        self.user12 = self.make_user(username='user_12')

        self.doctor = HealthTeam.objects.create(
            cpf="057.641.271-65",
            user=self.user2,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.doctor_2 = HealthTeam.objects.create(
            cpf="421.549.920-80",
            user=self.user6,
            speciality=HealthTeam.CARDIOLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234577",
            registration_state=HealthTeam.DF,
        )

        self.doctor_3 = HealthTeam.objects.create(
            cpf="084.684.390-02",
            user=self.user7,
            speciality=HealthTeam.PEDIATRICS,
            council_acronym=HealthTeam.CRM,
            register_number="1234447",
            registration_state=HealthTeam.DF,
        )

        self.doctor_4 = HealthTeam.objects.create(
            cpf="662.855.400-71",
            user=self.user8,
            speciality=HealthTeam.SPEECH_THERAPHY,
            council_acronym=HealthTeam.CREFONO,
            register_number="4434447",
            registration_state=HealthTeam.DF,
        )

        self.doctor_5 = HealthTeam.objects.create(
            cpf="705.246.660-08",
            user=self.user9,
            speciality=HealthTeam.PHYSIOTHERAPY,
            council_acronym=HealthTeam.CREFITO,
            register_number="4474447",
            registration_state=HealthTeam.DF,
        )

        self.doctor_6 = HealthTeam.objects.create(
            cpf="320.663.380-01",
            user=self.user10,
            speciality=HealthTeam.PSYCHOLOGY,
            council_acronym=HealthTeam.CRP,
            register_number="5474447",
            registration_state=HealthTeam.DF,
        )

        self.doctor_7 = HealthTeam.objects.create(
            cpf="736.358.660-83",
            user=self.user11,
            speciality=HealthTeam.GENERAL_PRACTITIONER,
            council_acronym=HealthTeam.CRM,
            register_number="9474447",
            registration_state=HealthTeam.DF,
        )

        self.doctor_8 = HealthTeam.objects.create(
            cpf="574.422.400-97",
            user=self.user12,
            speciality=HealthTeam.OCCUPATIONAL_THERAPY,
            council_acronym=HealthTeam.CREFITO,
            register_number="9974447",
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
        )



        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user,
            mother_name="Mother",
            father_name="Father",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible= self.responsible
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

    def test_request_create_view_responsible(self):
        """
        Makes sure that the request create view is loaded correctly
        """
        self.client.force_login(user=self.user4)
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

    def test_request_form_valid(self):
        """
        Test if risk speciality is the same of request speciality
        """
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.CARDIOLOGY,
            'doctor': self.doctor_2.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_cardiology,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.NEUROLOGY,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.NEUROLOGY,
            'doctor': self.doctor.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_neurology,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.PEDIATRICS,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.PEDIATRICS,
            'doctor': self.doctor_3.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_pediatrics,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

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
            'doctor': self.doctor_4.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_speech_theraphy,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.PHYSIOTHERAPY,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.PHYSIOTHERAPY,
            'doctor': self.doctor_5.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_physiotherapy,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.PSYCHOLOGY,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.PSYCHOLOGY,
            'doctor': self.doctor_6.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_psychology,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.GENERAL_PRACTITIONER,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.GENERAL_PRACTITIONER,
            'doctor': self.doctor_7.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': self.patient.risk.priority_general_practitioner,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

        request = AppointmentRequest.objects.create(
            shift=AppointmentRequest.MORNING,
            day=AppointmentRequest.MONDAY,
            speciality=AppointmentRequest.GENERAL_PRACTITIONER,
            doctor=self.doctor,
            patient=self.patient,
            status=AppointmentRequest.PENDING
        )
        self.client.force_login(user=self.user3)
        data = {
            'speciality': Appointment.OCCUPATIONAL_THERAPY,
            'doctor': self.doctor_8.pk,
            'patient': self.patient.pk,
            'day': AppointmentRequest.MONDAY,
            'shift': AppointmentRequest.MORNING,
            'status': AppointmentRequest.PENDING,
            'risk': 5,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:create_request',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)
        data = {
            'speciality': Appointment.PSYCHOLOGY,
        }
        response = self.client.post(
            path=reverse(
                viewname='appointments:ajax_load_doctors',
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/doctors_dropdown_list_options.html')

