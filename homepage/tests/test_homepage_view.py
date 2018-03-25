from django.test import TestCase, Client
from django.urls import reverse, resolve
from homepage.views import index

# Create your tests here.


class HomepageTestCase(TestCase):

    def setUp(self):
        """
            Prepares data for tests
        """

        self.client = Client()

    def test_homepage_view_success_status_code(self):
        """
            Checks if homepage view is loaded successfully
        """

        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_index_view(self):
        """
            Checks if the '/' url is returning the homepage view
        """

        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'homepage/index.html')
