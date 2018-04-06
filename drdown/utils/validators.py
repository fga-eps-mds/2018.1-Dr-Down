import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def validate_cpf(value):
    """
        validate a CPF passed as a string, checks for correct format and
         valida math
    """

    # regex to check if CPF is XYZ.XYZ.XYZ-XX (X is a nunber from 0 to 9)
    regex_code = r"[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}"
    regex_validator = RegexValidator(
        regex=regex_code,
        message=_('Wrong CPF format'))

    # this will raise an exception in case of failure
    regex_validator(value)

    # regex to check if CPF has all numbers equal
    regex_code_all_equal = r"([\d])\1\1[.]([\d])\2\2[.]([\d])\3\3[-]([\d])\4"

    # this time, we will set inverse_match to true,
    # because we wan't to check if the CPF is
    # out of the range
    regex_validator = RegexValidator(
        regex=regex_code_all_equal,
        message=_('This CPF is not permited'),
        inverse_match=True
    )

    regex_validator(value)

    # we need to check the math behind a cpf
    # first step is to get rid of the punctuation
    cpf_numbers_string = re.sub(r'[.]?[-]?', '', value)

    # and convert to a format more easy to work with
    cpf_numbers = list(map(lambda x: int(x), cpf_numbers_string))

    # the first 9 are alreadly calculated
    cpf_calculated = cpf_numbers[:9]

    # now we do the math
    # we need to multiply the first 9 numbers
    # by 10 to 2 (from the first to the last) and we sum them
    cpf_first_sum = cpf_second_sum = 0
    for i in range(0, 9):
        cpf_first_sum += cpf_numbers[i] * (10 - i)
        cpf_second_sum += cpf_numbers[i] * (11 - i)

    # we divide the sum by 11 and get the mod
    # and apply the rules
    cpf_calculated.append(calculate_cpf_verification_digit(cpf_first_sum))

    # now we have the starting 9 digits and 1 calculated, so we have 10 digits
    # on total to find the second verification digit we need to make the
    # calculation with the first validation number added
    cpf_second_sum += cpf_numbers[9] * 2

    cpf_calculated.append(calculate_cpf_verification_digit(cpf_second_sum))

    # now we check if the calculated cpf is the same as the informed

    if cpf_numbers != cpf_calculated:
        raise ValidationError(
            _('%(value)s is a invalid CPF, the verification digit is wrong'),
            params={'value': value}
        )


def calculate_cpf_verification_digit(sum):
    digit = 0

    if (sum % 11) >= 2:
        digit = (11 - (sum % 11))

    return digit
