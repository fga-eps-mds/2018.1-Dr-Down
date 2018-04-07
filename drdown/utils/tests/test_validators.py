from django.test import TestCase
from django.core.exceptions import ValidationError

from drdown.utils.validators import validate_cpf, validate_ses,\
    validate_generic_number, validate_names, validate_sus


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
            "999.999.999-99"
        ]

        for i in range(0, wrong_test_values.__len__()):
            with self.assertRaises(ValidationError, msg=wrong_test_values[i]):
                validate_cpf(wrong_test_values[i])

        # test if cfp is rigth
        try:
            validate_cpf(value="974.220.200-16")
        except ValidationError as error:
            self.fail(msg=error.message)

    def test_validate_ses(self):

        wrong_test_values = [
            "12345678",
            "123456",
            "1123456789",
            "12345",
            "1234",
            "123",
            "12",
            "1",
            "0",
            "111111111",
            "1111111",
            "122345",
            "asdqweqwe",
            "qweqweq",
            "qwe123qwe",
            "qwe1234",
            "12345678Z",
            "123456Z",
            ""
        ]

        for i in range(0, wrong_test_values.__len__()):
            with self.assertRaises(ValidationError, msg=wrong_test_values[i]):
                validate_ses(wrong_test_values[i])

        # test if ses is rigth
        try:
            validate_ses(value="000796544")
        except ValidationError as error:
            self.fail(msg=error.message)

    def test_validate_generic_number(self):

        wrong_test_values = [
            "11234567890123",
            "asdqweqwe",
            "qweqweq",
            "qwe123qwe",
            "qwe1234",
            "12345678Z",
            "123456Z",
            ""
        ]

        for i in range(0, wrong_test_values.__len__()):
            with self.assertRaises(ValidationError, msg=wrong_test_values[i]):
                validate_generic_number(wrong_test_values[i])

        # test a valid number
        try:
            validate_generic_number(value="000796544")
        except ValidationError as error:
            self.fail(msg=error.message)

    def test_valid_names(self):

        wrong_test_values = [
            "11234567890123",
            "João ",
            "João2 da silva",
            "João da silva ",
            "123",
            ""
        ]

        for i in range(0, wrong_test_values.__len__()):
            with self.assertRaises(ValidationError, msg=wrong_test_values[i]):
                validate_names(wrong_test_values[i])

        # test a valid number
        try:
            validate_names(value="João da Silva")
        except ValidationError as error:
            self.fail(msg=error.message)

    def test_valid_sus(self):

        wrong_test_values = [
            "12345678",
            "123456",
            "1123456789",
            "12345",
            "1234",
            "123",
            "12",
            "1",
            "0",
            "12345678912345",
            "1234567891234",
            "123456789123",
            "12345678912",
            "111111111111111",
            "asdasdasdasdasd",
            "asdasdasdasd123",
            "asdas123dasdasd",
            ""
        ]

        for i in range(0, wrong_test_values.__len__()):
            with self.assertRaises(ValidationError, msg=wrong_test_values[i]):
                validate_sus(wrong_test_values[i])

        # test a valid number
        try:
            validate_sus(value="123456789123456")
        except ValidationError as error:
            self.fail(msg=error.message)

