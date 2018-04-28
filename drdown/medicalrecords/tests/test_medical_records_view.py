from test_plus.test import TestCase
from ..models.model_medical_record import MedicalRecord
from ..views.view_medical_record import MedicalRecordsSearchList
from ..views.view_medical_record import MedicalRecordCompleteSearchForm
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from drdown.users.models.model_user import User
from django.test.client import Client
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class TestViewMedicalRecords(TestCase):

    def setUp(self):
        """
        This method will run before any test case.
        """

        self.client = Client()
        self.user_1 = self.make_user()
        self.user_2 = self.make_user(username="teste_2")
        self.user_3 = self.make_user(username="teste_3")
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
        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:create_medicalrecords',
                args=(self.patient.user.username,)
            ),
            data={'form': {'message': "", 'author': 'self.user'}},
        )
        self.assertFormError(response, 'form', 'message', _('This field is required.'))
        self.assertEquals(response.status_code, 200)

    def test_delete_medical_records_ok(self):
        """
        Test is medical records is being correcty updated.
        """

        self.client.force_login(user=self.user_1)



        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:delete_medicalrecords',
                args=(self.patient.user.username,self.medicalrecord.pk,)
            ),
            follow=True
        )

        self.assertEquals(
            response.status_code,
           200
        )

    def test_updated_medical_records_ok(self):
        """
        Test is medical records is being correcty updated.
        """

        self.client.force_login(user=self.user_1)

        data = {
            'message': 'test',
            'patient': 'self.patient',
            'author': 'self.user_1',
            'document': 'test.txt',
        }

        response = self.client.post(
            path=reverse(
                viewname='medicalrecords:update_medicalrecords',
                args=(self.patient.user.username,self.medicalrecord.pk,)
            ),
            follow=True,
            data=data
        )

        self.assertEquals(response.status_code,200)

    def test_search_list_view(self):
        """
        Makes sure that the medicalrecord search view is loaded correctly
        """

        self.client.force_login(user=self.user_1)
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_search_medicalrecords',
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_search_list_view_logout(self):
        """
        Makes sure that the medicalrecord search view gives 302 on a logout
        """

        self.client.force_login(user=self.user_1)
        self.client.logout()
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_search_medicalrecords',
            )
        )
        self.assertEquals(response.status_code, 302)

    def test_search_list_view_no_permissions(self):
        """
        Makes sure that the medicalrecord gives 302 on a user without
        permissions
        """

        self.client.force_login(user=self.user_2)
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='medicalrecords:list_search_medicalrecords',
            )
        )
        self.assertEquals(response.status_code, 302)

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
