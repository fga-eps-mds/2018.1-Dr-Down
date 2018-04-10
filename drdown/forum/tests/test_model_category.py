from test_plus.test import TestCase
from ..models.model_category import Category


class ModelTestCase(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name='Medicamentos',
            description='Tipo de Medicamento',

        )

        self.category2 = Category.objects.create(
            name='Eventos',
            description='Tipo de Eventos',

        )

    def tearDown(self):

        self.category1.delete()
        self.category2.delete()

    def test_save_name_ok(self):
        self.assertEquals(self.category1.name, 'Medicamentos')
        self.assertEquals(self.category2.name, 'Eventos')

    def test_save_description_ok(self):
        self.assertEquals(self.category1.description, 'Tipo de Medicamento')
        self.assertEquals(self.category2.description, 'Tipo de Eventos')

    def test_save_name_error(self):
        self.assertNotEquals(self.category1.name, '')
        self.assertNotEquals(self.category2.name, '')

    def test_save_description_error(self):
        self.assertNotEquals(self.category1.description, '')
        self.assertNotEquals(self.category2.description, '')
