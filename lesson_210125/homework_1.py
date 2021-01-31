numbers = {chr(el) for el in range(ord('0'), ord('9') + 1)}
numbers.update(['/', '-', '.'])

required_numbers = {'/'}
required_numbers_1 = {'-'}
required_numbers_2 = {'.'}


def data_is_valid(data):
    global data1
    data_is_set = set(data)

    if not data or data_is_set - numbers or required_numbers - data_is_set:
        if not data or data_is_set - numbers or required_numbers_1 - data_is_set:
            if not data or data_is_set - numbers or required_numbers_2 - data_is_set:
                return False

    for data1 in required_numbers:
        count = data.count(data1)
        if count != 2:
            for data1 in required_numbers_1:
                count = data.count(data1)
                if count != 2:
                    for data1 in required_numbers_2:
                        count = data.count(data1)
                        if count != 2:
                            return False

    day, month, year = data.split(data1)
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