# Higher Order functions:
# A higher order function is a function that takes another function as an argument, or returns a function as a result

import math


def add_nums(num):
    return sum(num)

numbers = [1, 2, 3, 4, 5]
print(add_nums(numbers))

def square_nums(num):
    return math.floor(math.pow(num, 2))


print(square_nums(283))