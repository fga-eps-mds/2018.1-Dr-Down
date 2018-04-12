from test_plus.test import TestCase
from django.test.client import Client
from ..models.model_category import Category
from ..models.model_post import Post
from ..models.model_commentary import Commentary
from django.urls import reverse, resolve


class TestViewPost(TestCase):

    def setUp(self):
        """
               This method will run before any test case.
        """

        self.client = Client()
        self.user = self.make_user()
        self.category = Category.objects.create(
            name="Test Category",
            description="Making a category for post test case",
            slug="test-slug"
        )
        self.post = Post.objects.create(
            title="Test Post",
            message="Making a post test case",
            created_by=self.user,
            category=self.category,
        )

        self.commentary = Commentary.objects.create(
            message='abcde',
            post=self.post,
            updated_at='2018-06-09',
            created_by=self.user,
            updated_by=self.user,
            slug='test',
        )

        self.url = "{% url 'forum:list_commentary' self.category.slug self.category.pk self.post.pk%}"
        self.commentary.save()

    def test_commentary_list_view(self):
        """
        Makes sure that the commentary list view is loaded correctly
        """
        response = self.client.get(
            reverse('forum:list_commentary', args=(self.category.slug, self.category.pk, self.post.pk)))
        self.assertEquals(response.status_code, 200)

    def test_commentary_create_view(self):
        """
        Makes sure that the commentary create view is loaded correctly
        """
        response = self.client.get(reverse('forum:create_commentary', args=(self.category.slug, self.category.pk, self.post.pk)))
        self.assertEquals(response.status_code, 200)

    def test_commentary_update_view(self):
        """
        Makes sure that the post commentary view is loaded correctly
        """
        response = self.client.get(reverse('forum:update_commentary', args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)))
        self.assertEquals(response.status_code, 200)

    def test_commentary_delete_view(self):
        """
        Makes sure that the commentary update view is loaded correctly
        """
        response = self.client.get(reverse('forum:delete_commentary', args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)))
        self.assertEquals(response.status_code, 200)
