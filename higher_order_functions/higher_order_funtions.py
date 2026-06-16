# # Higher Order functions:
# # A higher order function is a function that takes another function as an argument, or returns a function as a result

# import math


# def add_nums(num):
#     return sum(num)

# numbers = [1, 72, 3, 94, 55]
# # print(add_nums(numbers))

# def square_nums(num):
#     return math.floor(math.pow(num, 2))


# # print(square_nums(283))

# def higher_od_func(f,lst):
#     result = f(lst)
#     return result

# test_func = higher_od_func(add_nums,numbers)

# print(test_func)


# # closures : A closure is a function object that has access to variables in its enclosing scope, 
# # even after the outer function has finished executing.

# def outer_func(x):
#     def inner_func(y):
#         return x + y
#     return inner_func

# add_number = outer_func(524)
# print(add_number(5))


# arr = [1,2,3,4]

# for i in arr:
#     print(f".{i}")

# def sum_numbers(num):
#     result = 0
#     for i in arr :
#         result += i
#     return result


# print(sum_numbers(arr))

# def higher_order_function(f, num):
#     result = f(num)
#     return result ** 2


# print(higher_order_function(sum_numbers,arr))

# MAP FUNCTIONS
arr = [1,2,3,4,5]

def square(nums):
    result = nums ** 2
    return result
    

mapped_func = map(square,arr)
print(list(mapped_func))


text = 'python'

def uppercase(text):
    result = text.upper()
    return result;

map_text = map(uppercase, text)

print(list(map_text))


# FILTER IN PYTHON
numbers = [1,2,3,4,5,6,7,8,9]

def is_even(num):
    if num % 2 == 0:
        return True
    return False

check_num = filter(is_even, numbers)
print(list(check_num))