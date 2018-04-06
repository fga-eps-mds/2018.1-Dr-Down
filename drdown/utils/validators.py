import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def validate_cpf(value):
    """
        validate a CPF passed as a string, checks for correct format and valida math
    """

    # regex to check if CPF is XYZ.XYZ.XYZ-XX (X is a nunber from 0 to 9)
    regex_code = r"[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}"
    regex_validator = RegexValidator(regex=regex_code, message=_('Wrong CPF format'))

    # this will raise an exception in case of failure
    regex_validator(value)

    # regex to check if CPF has all numbers equal
    regex_code_all_equal = r"([\d])\1\1[.]([\d])\2\2[.]([\d])\3\3[-]([\d])\4"

    # this time, we will set inverse_match to true, because we wan't to check if the CPF is
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
    cpf_numbers = []

    for i in range(0, cpf_numbers_string.__len__()):
        cpf_numbers.append(int(cpf_numbers_string[i]))

    cpf_calculated = cpf_numbers[0:9]

    # now we do the math
    # we need to multiply the first 9 numbers by 10 to 2 (from the first to the last)
    # and we sum them
    cpf_sum = 0
    for i in range(0, cpf_calculated.__len__()):
        cpf_sum += cpf_numbers[i] * (10-i)

    # we divide the sum by 11 and get the mod
    mod = cpf_sum % 11

    # and apply the rules
    if mod < 2:
        cpf_calculated.append(0)
    else:
        cpf_calculated.append(11-mod)

    # now we have the starting 9 digits and 1 calculated, so we have 10 digits on total
    # to find the second verification digit we need to make the same process, but with 10 numbers

    cpf_sum = 0
    for i in range(0, cpf_calculated.__len__()):
        cpf_sum += cpf_numbers[i] * (11-i)

    mod = cpf_sum % 11

    if mod < 2:
        cpf_calculated.append(0)
    else:
        cpf_calculated.append(11-mod)

    # now we check if the calculated cpf is the same as the informed

    if cpf_numbers != cpf_calculated:
        raise ValidationError(
            _('%(value)s is a invalid CPF, the verification digit is wrong'),
            params={'value': value}
        )

def validate_phone(value):

    regex_code = r"[(][\d]{2}[)][\d]{4,5}[-][\d]{4}"
    regex_validator = RegexValidator(regex=regex_code, message=_('Wrong phone format'))

    # this will raise an exception in case of failure
    regex_validator(value)