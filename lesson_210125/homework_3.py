import re

RE_NUMBER_VALIDATOR = re.compile(r'^[0-9]{1,}[.,][0-9]{1,}$')


def number_is_valid(number):
    return RE_NUMBER_VALIDATOR.match(number)



assert number_is_valid('155,552')
assert number_is_valid('1.55')
assert number_is_valid('1,5555')
assert not number_is_valid('155')
assert not number_is_valid('155afw')
assert not number_is_valid('155=')
assert number_is_valid('155,0')
assert not number_is_valid('155/0'), 'Ваше число не вещественное'

