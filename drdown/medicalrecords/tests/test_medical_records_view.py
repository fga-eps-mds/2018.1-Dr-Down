from test_plus.test import TestCase
from ..models.model_medical_record import MedicalRecord
from ..views.view_medical_record import MedicalRecordsSearchList
from ..views.view_medical_record import MedicalRecordCompleteSearchForm
from drdown.users.models.model_patient import Patient
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
        self.user = self.make_user()
        self.patient = Patient.objects.create(
                     ses="1234567",user=self.user, priority=1,
                     mother_name="Mae", father_name="Pai",ethnicity=3,
                     sus_number="12345678911",
                     civil_registry_of_birth="12345678911",
                     declaration_of_live_birth="12345678911"
        )
        self.medicalrecord = MedicalRecord.objects.create(
            day="05-09-1998",
            message="Making a post test case",
            patient=self.patient,
            author=self.user,
            document="test.txt",
        )
        self.medicalrecord.save()
        self.patient.save()


    def test_post_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user)
        data = {
            'message': 'test',
            'patient': 'self.patient',
            'author': 'self.user',
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

        self.client.force_login(user=self.user)



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

        self.client.force_login(user=self.user)

        data = {
            'message': 'test',
            'patient': 'self.patient',
            'author': 'self.user',
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
            Makes sure that the post search view is loaded correctly
            """
            self.url = ()
            response = self.client.get(
                path=reverse(
                    viewname='medicalrecords:list_search_medicalrecords',
                )
            )
            self.assertEquals(response.status_code, 200)


