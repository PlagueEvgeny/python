def str_len(func):
    def inner(len_check):
        print(f' Количество символов в строке: {len(len_check)}')
        return func(len_check)

    return inner


@str_len
def parse_str(src_str):
    return src_str.strip().split()


sample_1 = 'идет февраль месяц, скоро весна'
sample_1_p = parse_str(sample_1)
print(sample_1_p)

sample_2 = 'идет февраль'
sample_2_p = parse_str(sample_2)
print(sample_2_p)


def word():
    with open("decorators.txt", 'r', encoding='utf-8') as decor:
        word_read = decor.read()
        word_read_parse = parse_str(word_read)

    return word_read_parse


print(word())

