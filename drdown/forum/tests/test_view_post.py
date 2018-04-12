from test_plus.test import TestCase
from django.test.client import Client
from ..models.model_category import Category
from ..models.model_post import Post
from django.urls import reverse, resolve


class TestViewPost(TestCase):

    def setUp(self):
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
        self.url = "{% url 'forum:list_posts' self.category.slug self.category.pk %}"
        self.post.save()

    def test_post_list_view(self):
        """
        Makes sure that the post list view is loaded correctly
        """
        response = self.client.get(reverse('forum:list_posts', args=(self.category.slug, self.category.pk)))
        self.assertEquals(response.status_code, 200)

    def test_post_create_view(self):
        """
        Makes sure that the post create view is loaded correctly
        """
        response = self.client.get(reverse('forum:create_post', args=(self.category.slug, self.category.pk)))
        self.assertEquals(response.status_code, 200)

    def test_post_update_view(self):
        """
        Makes sure that the post update view is loaded correctly
        """
        response = self.client.get(reverse('forum:update_post', args=(self.category.slug, self.category.pk, self.post.pk)))
        self.assertEquals(response.status_code, 200)

    def test_post_delete_view(self):
        """
        Makes sure that the post update view is loaded correctly
        """
        response = self.client.get(reverse('forum:delete_post', args=(self.category.slug, self.category.pk, self.post.pk)))
        self.assertContains(response, text=self.post.title)

    def test_form(self):
        response = self.client.post(
            reverse('forum:create_post', args=(self.category.slug, self.category.pk)),
            data={'form': {'title': "",'message': "Making a post test case", 'user':'self.user' }},
        )
        self.assertFormError(response, 'form', 'title', 'This field is required.')
        self.assertEquals(response.status_code, 200)

