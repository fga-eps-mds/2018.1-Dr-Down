from test_plus.test import TestCase
from django.test.client import Client
from ..models.model_category import Category
from ..models.model_post import Post
from django.urls import reverse, resolve
from datetime import datetime

from django.utils.translation import ugettext_lazy as _

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
        self.post.save()

    def test_post_list_view(self):
        """
        Makes sure that the post list view is loaded correctly
        """
        self.url = ()
        response = self.client.get(
            path=reverse(
                viewname='forum:list_posts',
                args=(self.category.slug, self.category.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_post_create_view(self):
        """
        Makes sure that the post create view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:create_post',
                args=(self.category.slug, self.category.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_post_update_view(self):
        """
        Makes sure that the post update view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:update_post',
                args=(self.category.slug, self.category.pk, self.post.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_post_delete_view(self):
        """
        Makes sure that the post update view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:delete_post',
                args=(self.category.slug, self.category.pk, self.post.pk)
            )
        )
        self.assertContains(response, text=self.post.title)

    def test_form_invalid(self):
        """
        Test if form is valid with blank fields
        """
        response = self.client.post(
            path=reverse(
                viewname='forum:create_post',
                args=(self.category.slug, self.category.pk)
            ),
            data={'form': {'title': "",'message': "Making a post test case", 'user':'self.user'}},
        )
        self.assertFormError(response, 'form', 'title', _('This field is required.'))
        self.assertEquals(response.status_code, 200)

    def test_post_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
        """
        self.client.force_login(user=self.user)
        data = {
            'title': 'Test',
            'message': 'hello test',
            'category': 'self.category',
            'created_at': 'datetime.now',
            'slug': 'test',
        }
        response = self.client.post(
            path=reverse(
                viewname='forum:create_post',
                args=(self.category.slug, self.category.pk)
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_post_form_valid_update_view(self):
        """
        Test if update form is valid with all required fields
        """
        self.client.force_login(user=self.user)
        data = {
            'title': 'Test',
            'message': 'hello test',
            'category': 'self.category',
            'created_at': 'datetime.now',
            'slug': 'test',
        }
        response = self.client.post(
            path=reverse(
                viewname='forum:update_post',
                args=(self.category.slug, self.category.pk, self.post.pk)
            ),
            data=data,
            follow=True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_delete_ok(self):
            """
            Test the home page url status code.
            """

            self.client.force_login(user=self.user)
            data = {
                'message': 'hello test',
                'post': 'self.post',
                'created_at': 'datetime.now',
                'slug': 'test',
            }

            response = self.client.post(
                path=reverse(
                    viewname='forum:delete_post',
                    args=(self.category.slug, self.category.pk, self.post.pk)
                ),
                data=data,
                follow=True
            )
            self.assertRedirects(
                response,
                reverse(
                    viewname='forum:list_posts',
                    args=(self.category.slug, self.category.pk)
                ),
                status_code=302,
                target_status_code=200
            )
