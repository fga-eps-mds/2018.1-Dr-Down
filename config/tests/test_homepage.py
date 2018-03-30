from django.test import TestCase, Client
from django.urls import reverse


class HomepageTestCase(TestCase):

    def setUp(self):
        """
            Prepares data for tests
        """

        self.client = Client() 

    def test_homepage_view_success_status_code(self): 
        """
            Checks if 'About SD' view is loaded successfully
        """

        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_index_view(self):
        """
            Checks if the '/info' url is returning the 'About SD' view
        """

        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'pages/info.html')
