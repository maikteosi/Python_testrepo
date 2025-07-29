import math


def square(side):
    area = side ** 2
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)


print(square(7.2))
