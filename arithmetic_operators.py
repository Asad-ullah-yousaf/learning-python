# Using Math functions and arithemetic operators in python is easy and straightforward. 
# We can perform basic arithmetic operations like addition, subtraction, multiplication, and division using the respective operators.

number = 1
# number = number + 1 # addition
number += 1 # this is a shorthand/augmented assignment for addition
print("After addition:", number)

number -= 1 # this is a shorthand/augmented assignment for subtraction
print("After subtraction:", number)

number *= 2 # this is a shorthand/augmented assignment for multiplication
print("After multiplication:", number)

number /= 2 # this is a shorthand/augmented assignment for division
print("After division:", number)

print("---------------------------------------")

# Python's built-in Math functions
x = 3.14
y = 4
z = 5

result = pow(y, 2) # this is the same as y ** 2
print("Power:", result)

result = abs(x) # this is the absolute value of x
print("Absolute value:", result)

result = round(x) # this rounds x to the nearest integer
print("Rounded value:", result)

result = max(x, y, z) # this returns the maximum value among x, y, and z
print("Maximum value:", result)

result = min(x, y, z) # this returns the minimum value among x, y, and z
print("Minimum value:", result)

print("---------------------------------------")