from test_plus.test import TestCase
from drdown.forum.models.model_category import Category


class ModelTestCase(TestCase):

    def setUp(self):
        """
            This method will run before any test case.
        """

        self.category1 = Category.objects.create(
            name='Medicamentos',
            description='Tipo de Medicamento',
            slug='med',

        )

        self.category2 = Category.objects.create(
            name='Eventos',
            description='Tipo de Eventos',
            slug='event',

        )

    def tearDown(self):
        """
            This method will run after any test.
        """

        self.category1.delete()
        self.category2.delete()

    def test_save_name_ok(self):
        """
            Test to verify if name of category is the correct passed
        """

        self.assertEquals(self.category1.name, 'Medicamentos')
        self.assertEquals(self.category2.name, 'Eventos')

    def test_save_description_ok(self):
        """
            Test to verify if description is the correct passed
        """

        self.assertEquals(self.category1.description, 'Tipo de Medicamento')
        self.assertEquals(self.category2.description, 'Tipo de Eventos')

    def test_save_slug_ok(self):
        """
            Test to verify if slug is the correct passed
        """
        self.assertEquals(self.category1.slug, 'med')
        self.assertEquals(self.category2.slug, 'event')

    def test_save_name_error(self):
        """
             Test to verify if name of category really fail
        """

        self.assertNotEquals(self.category1.name, '')
        self.assertNotEquals(self.category2.name, '')

    def test_save_description_error(self):
        """
            Test to verify if description really fail
        """

        self.assertNotEquals(self.category1.description, '')
        self.assertNotEquals(self.category2.description, '')

    def test_save_slug_error(self):
        """
             Test to verify if slug really fail
        """

        self.assertNotEquals(self.category1.slug, '')
        self.assertNotEquals(self.category2.slug, '')

    def test_str_is_equal_to_title(self):
        """
        Method `__str__` should be equal to field `title`
        """
        self.assertEqual(self.category1.__str__(), self.category1.name)
