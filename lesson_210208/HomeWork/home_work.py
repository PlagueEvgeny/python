import re
import random

valid_word = re.compile(r'\w+')


def word_is_valid(word):
    return valid_word.findall(word)


def word_randoms():
    with open('Skazka.txt', 'r', encoding='utf-8') as story:
        word_read = word_is_valid(story.read())
        # word_random = random.choice(word_read)
        while True:
            yield random.choice(word_read)


word_gen = word_randoms()
for _ in range(10):
    print(next(word_gen))




