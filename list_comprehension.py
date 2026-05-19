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

# ------------------------------------------

# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
new_lst = [i for i in numbers if i < 1]
print(new_lst)

# ------------------------------------------

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = []

print(flatten_list)
for i in list_of_lists:
    for x in i:
        flatten_list.append(x)
print(flatten_list)

new_lst = [x for i in list_of_lists for x in i]
print(new_lst)

# --------------------------------------

# Flattening the following List

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flatten_countries = [x for i in countries for x in i for x in x]
print(flatten_countries)

# --------------------------------------

# Convert into a dictionary

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Generic method
dictionary = []

for i in countries: 
    for country in i:
        dict = {'country':country[0], 'city':country[1]}
    dictionary.append(dict)
    
print(dictionary)
     
     
short_lst = [{'country':country[0], 'city':country[1]} for i in countries for country in i ]
print(short_lst)
     



        

    