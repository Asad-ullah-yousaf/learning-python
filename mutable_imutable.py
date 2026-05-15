# I am learning about mutable and immutable data types in python. 
# Mutable data types are those that can be changed after they have been created, 
# while immutable data types cannot be changed after they have been created.

# python treats strings as immutable data types which means we cannot change the value of a string after it has been created.
# But we can create a new string by concatenating two strings together or by slicing a string to create a new string.

username = 'Asad'
print(username[1])

# # List is a mutable data type which means we can change the values of a list after it has been created.
list1 = [1,2,3]
print(list1[1])

# # Tuple is an immutable data type which means we cannot change the values of a tuple after it has been created.
# # It differs from a list in that it is immutable and cannot be changed after it has been created. 
# # and it uses parantheses instead of square brackets.
tuple1 = (1,2,3)
print(tuple1[1])

# # Dictionary is a mutable data type which means we can change the values of a dictionary after it has been created.
# # we access values by keys instead of index like in lists and tuples.
object1 = {'name': 'Asad', 'age': 20}
print(object1['name'])

# # To check length of a list , tuple or dictionary 
# # we can use the len() function which returns the number of items in a list, tuple or dictionary.
length = len(list1)
print(length)

# Dictionaries are mutable data types which means we can change the values of a dictionary after it has been created.
dict = { 'name':'Asad', 'program' : 'Cyber Security' }
print(dict['name'])

x = dict.get('program')
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car)
print(car['brand'])

x = car.get('model')
print(x)

y = car.keys()
print(y)

car['year'] = 1977
print(car)


x = car.values()
print(x)

car['brand'] = 'Tesla'
print(x)


if 'model' in car:
  print(f"The model of this car is {car['model']}")
else:
  print("No Model Exists for this car")