from django.test import TestCase, Client
from django.urls import reverse, resolve
from homepage.views import index

# Create your tests here.


class HomepageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_view_success_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)