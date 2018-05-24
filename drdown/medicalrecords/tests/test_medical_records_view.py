from test_plus.test import TestCase
from django.core.exceptions import ValidationError
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_employee import Employee
from ..models.model_exams import Exam
from ..models.model_medical_record import MedicalRecord
from ..models.model_static_data import StaticData
from ..models.model_medicines import Medicine
from ..models.model_complaint import Complaint
from django.test.client import Client
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from unittest.mock import *


class TestViewMedicalRecords(TestCase):

    def setUp(self):
        """
        This method will run before any test case.
        """

        self.client = Client()
        self.user_1 = self.make_user()
        self.user_2 = self.make_user(username="teste_2")
        self.user_3 = self.make_user(username="teste_3")
        self.user_4 = self.make_user(username="teste_4")
        self.patient = Patient.objects.create(ses="1234567",
                                              user=self.user_2, priority=1,
                                              mother_name="Mãe",
                                              father_name="Pai",
                                              ethnicity=3,
                                              sus_number="123456789012345",
                                              civil_registry_of_birth="12345678911",
                                              declaration_of_live_birth="12345678911")

        self.health_team = HealthTeam.objects.create(
            cpf="507.522.730-94",
            user=self.user_1,
            council_acronym= 'CRM',
            register_number=123456789,
            registration_state='DF',
            speciality=HealthTeam.NEUROLOGY
        )

        self.medicalrecord = MedicalRecord.objects.create(
            day="05-09-1998",
            message="Making a post test case",
            patient=self.patient,
            author=self.health_team,
            document="test.txt",
        )

        self.complaint = Complaint.objects.create(
            created_at=timezone.datetime.today(),
            complaint_day=timezone.now() - timezone.timedelta(days=1),
            complaint_time='15:40',
            patient=self.patient,
            description="Não tô legal",
            author=self.health_team
        )

        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user_4,
            departament=Employee.ADMINISTRATION
        )

        self.exam = Exam.objects.create(
            patient=self.patient,
            day=timezone.now() - timezone.timedelta(days=1),
            category=1,
            file="exam.txt"
        )

        self.medicine = Medicine.objects.create(
            patient=self.patient,
            medicine_name="Neosaldina",
            medicine_dosage="2",
            medicine_in_use=True,
            author=self.health_team
        )

        self.staticdata = StaticData.objects.create(
            patient=self.patient,
            APGAR=9,
            weight=800,
            ear_test="text.txt",
            heart_test="teuxt.txt",
            author=self.health_team
        )

        self.medicalrecord.save()
        self.patient.save()


    def test_post_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user_1)
        data = {
            'message': 'test',
            'patient': 'self.patient',
            'author': 'self.user_1',
        }
        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:create_medicalrecords',
                args=(self.patient.user.username,)
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_form_invalid(self):
        """
        Test if form is valid with blank fields
        """
        self.client.force_login(user=self.user_1)
        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:create_medicalrecords',
                args=(self.patient.user.username,)
            ),
            data={'form': {'message': "", 'author': 'self.user'}},
        )
        self.assertFormError(response, 'form', 'message', _('This field is required.'))
        self.assertEquals(response.status_code, 200)

    def test_list_view(self):
        """
        Makes sure that the medicalrecord search view is loaded correctly
        """

        self.client.force_login(user=self.user_1)
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_medicalrecords',
                args=(self.patient.user.username,)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_list_view_employee(self):
        """
        Makes sure that the medicalrecord search view is loaded correctly
        """

        self.client.force_login(user=self.user_4)
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_medicalrecords',
                args=(self.patient.user.username,)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_list_view_logout(self):
        """
        Makes sure that the medicalrecord search view gives 302
        """

        self.client.force_login(user=self.user_1)
        self.client.logout()
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_medicalrecords',
                args=(self.patient.user.username,)
            )
        )
        self.assertEquals(response.status_code, 302)

    def test_list_view_no_permissions(self):
        """
        Makes sure that the patient can acess his medicalrecords
        """

        self.client.force_login(user=self.user_2)
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_medicalrecords',
                args=(self.patient.user.username,)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_list_view_not_specialized(self):
        """
        Makes sure that a user without permissions cannot
         acess a medicalrecords
        """

        self.client.force_login(user=self.user_3)
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_medicalrecords',
                args=(self.patient.user.username,)
            )
        )
        self.assertEquals(response.status_code, 302)

    def test_complaint_invalid_date(self):
        """
            Test if complaint day cannot be in future
        """


        with self.assertRaises(ValidationError):
            complaint = Complaint.objects.create(
                created_at=timezone.datetime.today(),
                complaint_day=timezone.now() + timezone.timedelta(days=1),
                complaint_time='15:40',
                patient=self.patient,
                description="Não tô legal",
                author=self.health_team
            )

            complaint.clean()

    def test_complaint_valid_date(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user_1)
        data = {
            'description': 'test',
            'complaint_day': timezone.now() - timezone.timedelta(days=1),
            'complaint_time': '10:40',
        }
        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:create_complaint_medicalrecords',
                args=(self.patient.user.username,)
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_exam_valid_date(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user_1)
        data = {
            'observation': 'test',
            'day': timezone.now() - timezone.timedelta(days=1),
            'file': 'text.txt'
        }
        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:create_exam_medicalrecords',
                args=(self.patient.user.username,)
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_exam_invalid_date(self):
        """
            Test if exam day cannot be in future
        """


        with self.assertRaises(ValidationError):
            complaint = Exam.objects.create(
                day=timezone.now() + timezone.timedelta(days=1),
                patient=self.patient,
                observations="Não tô legal",
                file="teuxt.txt",
            )

            complaint.clean()

    def test__str__(self):
        """
        This test check if __str__ is returning the data correctly.
        """

        self.assertEqual(self.medicalrecord.__str__(), 'teste_2')

        self.assertEqual(self.complaint.__str__(), 'teste_2 -  Comptaint ID: 1')

        self.assertEqual(
            self.exam.__str__(),
            str('teste_2 - ' + self.exam.get_category_display())
        )

        self.assertEqual(self.medicine.__str__(), 'teste_2 - Neosaldina')

        self.assertEqual(self.staticdata.__str__(), 'teste_2')
