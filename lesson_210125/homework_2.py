vnumber = {chr(el) for el in range(ord('0'), ord('9') + 1)}
vnumber.update([',', '.'])

required_number = {','}
required_number_1 = {'.'}


def number_is_valid(number):
    number_as_set = set(number)
    if not number or number_as_set - vnumber or required_number - number_as_set:
        if not number or number_as_set - vnumber or required_number_1 - number_as_set:
            return False


    number_chunks = number.split(',')
    number_chunks_1 = number.split('.')
    if len(number_chunks) < 2 or len(number_chunks[-1]) < 1:
        if len(number_chunks_1) < 2 or len(number_chunks_1[-1]) < 1:
            return False

    return True



assert number_is_valid('155,552')
assert number_is_valid('1.55')
assert number_is_valid('1,5555')
assert not number_is_valid('155')
assert not number_is_valid('155afw')
assert not number_is_valid('155=')
assert number_is_valid('155,0')
assert not number_is_valid('155/0'), 'Ваше число не вещественное'

