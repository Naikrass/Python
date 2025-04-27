import math
sq = float(input('Введите сторону квадрата: '))


def square(sq):
    return math.ceil(sq * sq)


print(square(sq))
