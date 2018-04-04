from django.test import TestCase
from django.core.exceptions import ValidationError

from drdown.utils.validators import validate_cpf


class TestValidator(TestCase):

    def test_validate_cpf(self):

        wrong_test_values = [
            "97422020016",
            "974.220.200.16",
            "974-220-200-16",
            "97.4220.200-16",
            "974..220.200-16",
            "974.220.200--16",
            "974.220.200-6",
            "974.220.200-00",
            "974.220.20a-16",
            "11974.220.200-16",
            "111.111.111-11",
            "222.222.222-22",
            "333.333.333-33",
            "444.444.444-44",
            "555.555.555-55",
            "666.666.666-66",
            "777.777.777-77",
            "888.888.888-88",
            "999.999.999-99",
            ""
        ]

        for i in range(0, wrong_test_values.__len__()):
            with self.assertRaises(ValidationError, msg=wrong_test_values[i]):
                validate_cpf(wrong_test_values[i])

        # test if cfp is rigth
        try:
            validate_cpf(value="974.220.200-16")
        except ValidationError as error:
            self.fail(msg=error.message)
