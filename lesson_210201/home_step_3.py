import cProfile
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp = temp // 10

    return num == reversed_num



# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     if pal:
#         print(pal)

cProfile.run('sum([i * 2 for i in range(10000)])')

