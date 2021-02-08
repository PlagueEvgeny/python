# endless sequence
a = range(5)
print(list(a))


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#     print(i, end=" ")


gen = infinite_sequence()
next(gen)

