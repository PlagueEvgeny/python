import re
import random

valid_word = re.compile(r'\w+')


def word_is_valid(word):
    return valid_word.findall(word)


def word_randoms():
    with open('Skazka.txt', 'r', encoding='utf-8') as story:
        word_read = word_is_valid(story.read())
        word_random = random.choices(word_read)
        while True:
            yield word_random
            word_random += word_read


for i in word_randoms():
    print(*i, end=' ')
    break


# word = word_randoms()
# while True:
#     print(*next(word))

