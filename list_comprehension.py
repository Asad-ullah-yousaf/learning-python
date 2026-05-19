# List comprehension is the shortest easiest way to create/Update a list

# normal list 
str = 'python'
lst = list(str)
print("normal list",lst)

# a comprehensiv list
str = [i for i in str]
print("Comprehensive list",str)

# generating list of numbers
lst_nums = [i for i in range(10)]
print("List of numbers", lst_nums)

# Lambda function is an anonymous function that can take any number of arguments but can only have one expression. 
# It is often used in conjunction with functions like map(), filter(), and reduce().

sum_nums = lambda a, b: a + b
sqr = lambda a:a*a
print(sum_nums(2,4), sqr(8))