
from test_plus.test import TestCase
from django.contrib.auth.models import Group

from drdown.forum.models.model_commentary import Commentary
from drdown.forum.models.model_post import Post
from drdown.forum.models.model_category import Category


class TestModelCommentary(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.category = Category.objects.create(
            name="abcc",
            description="cbaa",
        )
        self.post = Post.objects.create(
            title="abc",
            message="cba",
            category=self.category,
            created_by=self.user,
            updated_by=self.user,
            slug='test',
        )

        self.commentary = Commentary.objects.create(
            message='abcde',
            post=self.post,
            updated_at='2018-06-09',
            created_by=self.user,
            updated_by=self.user,
            slug='test',
        )

    def test_one_to_one_relation(self):
        self.assertIs(self.post, self.commentary.post)
        self.assertIs(self.user, self.post.created_by)
        self.assertIs(self.user, self.post.updated_by)

    def test_delete_cascade(self):

        self.assertEquals(Commentary.objects.get(
            message="abcde"), self.commentary)

        self.post.delete()

        with self.assertRaises(Commentary.DoesNotExist):
            Commentary.objects.get(message="abcde")


class ModelTestCase(TestCase):

    def setUp(self):
        self.user1 = self.make_user()
        self.category1 = Category.objects.create(
            name="abcc",
            description="cba",
        )
        self.post1 = Post.objects.create(
            title="abc",
            message="cba",
            category=self.category1,
            created_by=self.user1,
            updated_by=self.user1,
            slug='test',
        )

        self.commentary1 = Commentary.objects.create(
            message='abcde',
            post=self.post1,
            updated_at='2018-06-09',
            created_by=self.user1,
            updated_by=self.user1,
            slug='test',
        )

    def test_save_message_ok(self):
        self.assertEquals(self.commentary1.message, 'abcde')

    def test_save_post_ok(self):
        self.assertEquals(self.commentary1.post, self.post1)

    def test_save_updated_ok(self):
        self.assertEquals(self.commentary1.updated_at, '2018-06-09')

    def test_save_created_by_ok(self):
        self.assertEquals(self.commentary1.created_by, self.user1)

    def test_save_updated_by_ok(self):
        self.assertEquals(self.commentary1.updated_by, self.user1)

    def test_save_slug_ok(self):
        self.assertEquals(self.commentary1.slug, 'test')

    def test_save_post_error(self):
        self.assertNotEquals(self.commentary1.post, '')

    def test_save_message_error(self):
        self.assertNotEquals(self.commentary1.message, '')

    def test_save_updated_error(self):
        self.assertNotEquals(self.commentary1.updated_at, '')

    def test_save_created_by_error(self):
        self.assertNotEquals(self.commentary1.created_by, '')

    def test_save_updated_by_error(self):
        self.assertNotEquals(self.commentary1.updated_by, '')

    def test_save_slug_error(self):
        self.assertNotEquals(self.commentary1.slug, '')

