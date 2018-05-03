from test_plus.test import TestCase
from ..models.model_appointment import Appointment
from drdown.users.models.model_health_team import HealthTeam
from drdown.users.models.model_patient import Patient
from django.urls import reverse


class TestViewAppointment(TestCase):

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
            shift=Appointment.MORNING,
            date="2040-08-10",
            time="15:45",
            motive='Some motive',
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
        response = self.client.get(
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

    # def test_form_invalid(self):
    #     """
    #     Test if form is valid with blank fields
    #     """
    #     response = self.client.post(
    #         path=reverse(
    #             viewname='forum:create_post',
    #             args=(self.category.slug, self.category.pk)
    #         ),
    #         data={'form':
    #                   {'title': "",
    #                   'message': "Making a post test case",
    #                   'user':'self.user'}
    #         },
    #     )
    #     self.assertFormError(response, 'form', 'title', _('This field is required.'))
    #     self.assertEquals(response.status_code, 200)

    # def test_post_form_valid_create_view(self):
    #     """
    #     Test if create form is valid with all required fields
    #     """
    #     self.client.force_login(user=self.user)
    #     data = {
    #         'title': 'Test',
    #         'message': 'hello test',
    #         'category': 'self.category',
    #         'created_at': timezone.now(),
    #     }
    #     response = self.client.post(
    #         path=reverse(
    #             viewname='forum:create_post',
    #             args=(self.category.slug, self.category.pk)
    #         ),
    #         data=data,
    #         follow=True)
    #     self.assertEquals(response.status_code, 200)
    #
    # def test_post_form_valid_update_view(self):
    #     """
    #     Test if update form is valid with all required fields
    #     """
    #     self.client.force_login(user=self.user)
    #     data = {
    #         'title': 'Test',
    #         'message': 'hello test',
    #         'category': 'self.category',
    #         'created_at': timezone.now(),
    #     }
    #     response = self.client.post(
    #         path=reverse(
    #             viewname='forum:update_post',
    #             args=(self.category.slug, self.category.pk, self.post.pk)
    #         ),
    #         data=data,
    #         follow=True)
    #     self.assertEquals(response.status_code, 200)
    #
    # def test_redirect_delete_ok(self):
    #         """
    #         Test the home page url status code.
    #         """
    #
    #         self.client.force_login(user=self.user)
    #         data = {
    #             'message': 'hello test',
    #             'post': 'self.post',
    #             'created_at': timezone.now(),
    #         }
    #
    #         response = self.client.post(
    #             path=reverse(
    #                 viewname='forum:delete_post',
    #                 args=(self.category.slug, self.category.pk, self.post.pk)
    #             ),
    #             data=data,
    #             follow=True
    #         )
    #         self.assertRedirects(
    #             response,
    #             reverse(
    #                 viewname='forum:list_posts',
    #                 args=(self.category.slug, self.category.pk)
    #             ),
    #             status_code=302,
    #             target_status_code=200
    #         )
