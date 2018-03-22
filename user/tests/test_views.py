from django.urls import reverse
from django.test import TestCase

from user.models import User
# Create your tests here.


class UserViewTestCase(TestCase):
    def create_user(self, name="Joao", last_name="Silva",
                        email="user@example.com", password="12345678",
                        birthday="01/01/1997", gender="M",
                        telephone=12345678):
        return User.objects.create(name=name, last_name=last_name,
                            email=email, password=password,
                            birthday=birthday, gender=gender,
                            telephone=telephone)

    def test_list_view(self):
        list_url = reverse("list_users")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)

    
