from test_plus.test import TestCase
from django.test.client import Client
from ..models.model_curves import Curves
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_health_team import HealthTeam
from django.urls import reverse


class TestModelRequest(TestCase):

    WEIGHT = 10
    HEIGHT = 123
    CEPHALIC_PERIMETER = 30
    AGE = 1

    def setUp(self):
        """
        This method will run before any test case.
        """

        self.client = Client()

        self.user = self.make_user()

        self.patient = Patient.objects.create(
            ses="1234567",
            user=self.user,
            mother_name="Mãe",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
        )

        self.user2 = self.make_user(username='user2')

        self.health_team = HealthTeam.objects.create(
            cpf="057.641.271-65",
            user=self.user2,
            speciality=HealthTeam.NEUROLOGY,
            council_acronym=HealthTeam.CRM,
            register_number="1234567",
            registration_state=HealthTeam.DF,
        )

        self.curve = Curves.objects.create(
            patient=self.patient,
            weight=self.WEIGHT,
            height=self.HEIGHT,
            cephalic_perimeter=self.CEPHALIC_PERIMETER,
            age=self.AGE,
        )

    def test_appointment_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.health_team.user)

        data = {
            'height': self.HEIGHT,
            'weight': self.WEIGHT,
            'age': self.AGE,
            'cephalic_perimeter': self.CEPHALIC_PERIMETER,
        }

        response = self.client.post(
            path=reverse(
                'medicalrecords:create_curve',
                kwargs={'username': self.patient.user.username}
            ),
            data=data,
            follow=True
        )

        self.assertEquals(response.status_code, 200)

    def test_data_parse_curves_height(self):
        self.client.force_login(user=self.user2)
        self.client.request()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:curve_ajax',

            ),
            follow=True,
            data={'username': self.user.username, 'data_type': 'height','time_frame': 'months' }
        )
        self.assertEquals(response.status_code, 200)

    def test_data_parse_curves_weight(self):
        self.client.force_login(user=self.user2)
        self.client.request()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:curve_ajax',
            ),
            follow=True,
            data={'username': self.user.username, 'data_type': 'weight','time_frame': 'months' }
        )
        self.assertEquals(response.status_code, 200)

    def test_data_parse_curves_bmi(self):
        self.client.force_login(user=self.user2)
        self.client.request()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:curve_ajax',
            ),
            follow=True,
            data={'username': self.user.username, 'data_type': 'bmi', }
        )
        self.assertEquals(response.status_code, 200)

    def test_data_parse_curves_cephalic_perimeter(self):
        self.user.gender = "F"
        self.client.force_login(user=self.user2)
        self.client.request()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:curve_ajax',
            ),
            follow=True,
            data={'username': self.user.username, 'data_type': 'cephalic_perimeter', }
        )
        self.assertEquals(response.status_code, 200)
