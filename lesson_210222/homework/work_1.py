import re

valid_num = re.compile(r'\d+')


def word_is_valid(num):
    return valid_num.findall(num)


def seq_one():
    with open("one_seq.txt", "r", encoding="utf-8") as word:
        word_read = word_is_valid(word.read())
        for item in word_read:
            yield item


def seq_two():
    with open("two_seq.txt", "r", encoding="utf-8") as word:
        word_read = word_is_valid(word.read())
        for item in word_read:
            yield item


# def seq():
#     gen = [int_sq for int_sq in seq_one()]
#     gen_one = [int_sq_two for int_sq_two in seq_two()]
#     gen.remove()
#     print(gen)
#     print(gen_one)






# print(type(seq()))
# for _ in range(10):
#     print(next(gen))


# print(seq())

for _ in range(10):
    print(next(seq_two()))


for item in seq_two():
    print(item)


