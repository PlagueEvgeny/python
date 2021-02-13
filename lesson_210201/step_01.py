# https://github.com/PlagueEvgeny/python/blob/main/lesson_210125/homework_1.py
numbers = {chr(el) for el in range(ord('0'), ord('9') + 1)}
numbers.update(['/', '-', '.'])

required_numbers = {'/'}
required_numbers_1 = {'-'}
required_numbers_2 = {'.'}
_required_numbers = [{'/'}, {'-'}, {'.'}]
possible_splitters = ['/', '-', '.']



def data_is_valid(raw_data):

    data_as_set = set(raw_data)
    if not raw_data or data_as_set - numbers:
        if required_numbers - data_as_set or required_numbers_1 - data_as_set or \
                required_numbers_2 - data_as_set:
            return False


    for splitter in possible_splitters:
        if raw_data.count(splitter) == 2:
            break
    else:
        return False

    day, month, year = raw_data.split(splitter)
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False
    return True


assert data_is_valid('25.01.2021')
assert data_is_valid('25/01/2021')
assert data_is_valid('25-01-2021')
assert not data_is_valid('5.01.2021')
assert not data_is_valid('05.01.21')
assert not data_is_valid('05,01,2021')
assert not data_is_valid('05.01.21/')
assert not data_is_valid('05,01,,2021')

