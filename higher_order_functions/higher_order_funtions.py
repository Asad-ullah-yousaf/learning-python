# Higher Order functions:
# A higher order function is a function that takes another function as an argument, or returns a function as a result

import math


def add_nums(num):
    return sum(num)

numbers = [1, 72, 3, 94, 55]
# print(add_nums(numbers))

def square_nums(num):
    return math.floor(math.pow(num, 2))


# print(square_nums(283))

def higher_od_func(f,lst):
    result = f(lst)
    return result

test_func = higher_od_func(add_nums,numbers)

print(test_func)


# closures : A closure is a function object that has access to variables in its enclosing scope, 
# even after the outer function has finished executing.

def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

add_number = outer_func(524)
print(add_number(5))