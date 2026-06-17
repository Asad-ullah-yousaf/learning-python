# Exception Handling: We use Try except or try except else and finally to handle exceptions in our code. 
# It helps us to prevent our code from crashing and also helps us to provide a better user experience.
try:
    def sum(num1,num2):
        return print(num1 + num2)

    print(sum(2,'4'))
except:
    print("Error: Invalid input. Please provide two numbers.")
    
    
# List Unpacking
def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))

# Dictionary Unpacking
def print_user_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")
    
user_info = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print_user_info(**user_info)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.



# Extended Unpacking
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

cities = ['NewYork','LosAngles','Chicago','Washington']
new,los,*rest = cities
print(new,los,rest)


# Spreading in python
lst_one = [1,3,5,7,9]
lst_two = [2,4,6,8]
lst = [*lst_one, *lst_two]
print(lst)

# Enumerate
lst = [1,2,3,4]

for index,i in enumerate(lst):
    print(index,i)


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Norway':
        print(f"{i} is at {index} index in the Array")
    print(index,i)