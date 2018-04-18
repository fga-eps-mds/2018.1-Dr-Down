from test_plus.test import TestCase
from drdown.forum.models.model_commentary import Commentary
from drdown.forum.models.model_post import Post
from drdown.forum.models.model_category import Category
from django.utils import timezone


class TestModelCommentary(TestCase):

    def setUp(self):
        """
            This method will run before any test case.
        """

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
        )

        self.commentary = Commentary.objects.create(
            message='abcde',
            post=self.post,
            created_by=self.user,
        )

    def test_one_to_one_relation(self):
        """
            Test to verify if the relation it work
        """

        self.assertIs(self.post, self.commentary.post)
        self.assertIs(self.user, self.post.created_by)

    def test_delete_cascade(self):
        """
            Verify delete the relation objects
        """

        self.assertEquals(Commentary.objects.get(
            message="abcde"), self.commentary)

        self.post.delete()

        with self.assertRaises(Commentary.DoesNotExist):
            Commentary.objects.get(message="abcde")


class ModelTestCase(TestCase):

    def setUp(self):
        """
              This method will run before any test case.
        """

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
        )

        self.commentary1 = Commentary.objects.create(
            message='abcde',
            post=self.post1,
            created_by=self.user1,
        )

    def test_save_message_ok(self):
        """
            Test to verify if message is the correct passed
        """

        self.assertEquals(self.commentary1.message, 'abcde')

    def test_save_post_ok(self):
        """
            Test to verify if post is the correct passed
        """

        self.assertEquals(self.commentary1.post, self.post1)

    def test_save_created_by_ok(self):
        """
            Test to verify if created_by is the correct passed
        """

        self.assertEquals(self.commentary1.created_by, self.user1)

    def test_save_post_error(self):
        """
            Test to verify if post really fail
        """

        self.assertNotEquals(self.commentary1.post, '')

    def test_save_message_error(self):
        """
            Test to verify if message really fail
        """

        self.assertNotEquals(self.commentary1.message, '')

    def test_save_created_by_error(self):
        """
            Test to verify if created_by really fail
        """

        self.assertNotEquals(self.commentary1.created_by, '')


