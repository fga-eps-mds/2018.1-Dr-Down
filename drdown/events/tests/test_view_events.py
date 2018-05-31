from test_plus.test import TestCase
from django.urls import reverse, resolve
from drdown.events.models.model_events import Events
from drdown.users.models.model_employee import Employee
from drdown.users.models.model_health_team import HealthTeam

class TestViewEvents(TestCase):
	def setUp(self):
		self.user = self.make_user(username='user_1')
		self.user2 = self.make_user(username='user_2')
		self.employee = Employee.objects.create(
			cpf="974.220.200-16",
			user=self.user,
			departament=Employee.ADMINISTRATION
		)
		self.event = Events.objects.create(
			name="Palestra",
			time="20:00",
			date="2020-06-12",
			value="20",
			description="Palestra sobre SD",
			)

	def test_events_list_view(self):
		self.client.force_login(user=self.user)
		response = self.client.get(
			path=reverse(
				viewname='events:list_events'
			)
		)
		self.assertEquals(response.status_code, 200)

	def test_events_update_view_employee(self):
		self.client.force_login(user=self.user)

		response = self.client.get(
			path=reverse(
				viewname='events:update_event',
				args=(self.event.pk,)
			)
		)
		self.assertEquals(response.status_code, 200)

		response = self.client.post(
			path=reverse(
				viewname='events:update_event',
				args=(self.event.pk,)
			)
		)

	def test_events_create_view(self):
		self.client.force_login(user=self.user)

		response = self.client.post(
			path=reverse(
				viewname='events:create_event',
			)
		)
		self.assertEquals(response.status_code, 200)


