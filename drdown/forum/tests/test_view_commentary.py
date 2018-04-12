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

        self.commentary.save()

    def test_commentary_list_view(self):
        """
        Makes sure that the commentary list view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:list_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_commentary_create_view(self):
        """
        Makes sure that the commentary create view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:create_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_commentary_update_view(self):
        """
        Makes sure that the post commentary view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:update_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_commentary_delete_view(self):
        """
        Makes sure that the commentary update view is loaded correctly
        """
        response = self.client.get(
            path=reverse(
                viewname='forum:delete_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)
            )
        )
        self.assertEquals(response.status_code, 200)

    def test_form_invalid(self):
        """
        Test if form is valid with blank fields
        """
        response = self.client.post(
            path=reverse(
                viewname='forum:create_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            ),
            data={'form': {'message': "", 'user': 'self.user'}},
        )
        self.assertFormError(response, 'form', 'message', 'This field is required.')
        self.assertEquals(response.status_code, 200)

    def test_commentary_form_valid_create_view(self):
        """
        Test if create form is valid with all required fields
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
                viewname='forum:create_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            ),
            data=data,
            follow=True
        )
        self.assertEquals(response.status_code, 200)

    def test_commentary_form_valid_update_view(self):
        """
        Test if update form is valid with all required fields
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
                viewname='forum:update_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)
            ),
            data=data,
            follow=True
        )
        self.assertEquals(response.status_code, 200)

    def test_redirect_create_ok(self):
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
                viewname='forum:create_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            ),
            data=data,
            follow=True
        )
        # self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                'forum:list_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            ),
            status_code=302,
            target_status_code=200
        )

    def test_redirect_update_ok(self):
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
                viewname='forum:update_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)
            ),
            data=data,
            follow=True
        )
        # self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                'forum:list_commentary',
                args=(self.category.slug, self.category.pk, self.post.pk)
            ),
            status_code=302,
            target_status_code=200
        )

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
                    viewname='forum:delete_commentary',
                    args=(self.category.slug, self.category.pk, self.post.pk, self.commentary.pk)
                ),
                data=data,
                follow=True
            )
            # self.assertEqual(response.status_code, 302)
            self.assertRedirects(
                response,
                reverse(
                    'forum:list_commentary',
                    args=(self.category.slug, self.category.pk, self.post.pk)
                ),
                status_code=302,
                target_status_code=200
            )
