from test_plus.test import TestCase
from django.contrib.auth.models import Group

from drdown.forum.models.model_category import Category
from drdown.forum.models.model_post import Post


class TestModelPost(TestCase):

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
            created_at="1998-05-05",
            updated_at="1998-06-05",
            created_by=self.user,
        )

    def test_one_to_one_relation(self):
        """
            Test to verify if the relation it work
        """

        self.assertIs(self.category, self.post.category)
        self.assertIs(self.user, self.post.created_by)

    def test_delete_cascade(self):
        """
            Verify delete the relation objects
        """

        self.assertEquals(Post.objects.get(
            title="abc"), self.post)

        self.category.delete()

        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(title="abc")


class ModelTestCase(TestCase):

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
            created_at="1998-05-05",
            updated_at="1998-06-05",
            created_by=self.user,
        )

    def test_save_title_ok(self):
        """
        Test to verify if title is the correct passed
        """

        self.assertEquals(self.post.title, 'abc')

    def test_save_message_ok(self):
        """
        Test to verify if message is the correct passed
        """

        self.assertEquals(self.post.message, 'cba')

    def test_save_category_ok(self):
        """
        Test to verify if category is the correct passed
        """

        self.assertEquals(self.post.category, self.category)

    def test_save_updated_ok(self):
        """
        Test to verify if updated is the correct passed
        """

        self.assertEquals(self.post.updated_at, '1998-06-05')

    def test_save_created_by_ok(self):
        """
        Test to verify if created_by is the correct passed
        """

        self.assertEquals(self.post.created_by, self.user)

    def test_save_title_error(self):
        """
        Test to verify if title really fail
        """

        self.assertNotEquals(self.post.title, '')

    def test_save_message_error(self):
        """
        Test to verify if message really fail
        """

        self.assertNotEquals(self.post.message, '')

    def test_save_category_error(self):
        """
        Test to verify if category really fail
        """

        self.assertNotEquals(self.post.category, '')

    def test_save_updated_error(self):
        """
        Test to verify if updated really fail
        """

        self.assertNotEquals(self.post.updated_at, '1997-06-05')

    def test_save_created_by_error(self):
        """
        Test to verify if created_by really fail
        """
        self.assertNotEquals(self.post.created_by, '')


    def test_str_is_equal_to_title(self):
        """
        Method `__str__` should be equal to field `title`
        """

        self.assertEqual(self.post.__str__(), self.post.title)
