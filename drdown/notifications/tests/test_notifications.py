from test_plus.test import TestCase
from django.test.client import Client
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_responsible import Responsible
from django.urls import reverse
from drdown.forum.models.model_post import Post
from drdown.forum.models.model_category import Category
from django.utils import timezone

class TestViewNotifications(TestCase):

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
                                              user=self.user_2,
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

        self.responsible = Responsible.objects.create(
            user= self.user_3,
            cpf="065.770.581-05",
        )

        self.employee = Employee.objects.create(
            cpf="974.220.200-16",
            user=self.user_4,
            departament=Employee.ADMINISTRATION
        )

        self.category = Category.objects.create(
            name="abcc",
            description="cbaa",
        )

        self.post = Post.objects.create(
            title="abc",
            message="cba",
            category=self.category,
            created_at=timezone.datetime(1998, 5, 5),
            created_by=self.user_2,
        )




    def test_view_patient_notification(self):
        """
        Test go to notifications
        """
        self.client.force_login(user=self.user_2)
        response = self.client.get(
            path=reverse(
                viewname='notifications:patient_notifications',
            )
        )
        self.assertEquals(response.status_code, 200)
