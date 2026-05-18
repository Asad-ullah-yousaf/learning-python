# A function is a reusable block of code that can be used anywhere in the file once declared


def generate_my_name():
    first_name = "Asadullah"
    last_name = "yousaf"
    print(first_name + ' ' + last_name)
    

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
    
def generate_my_name(first_name, last_name):
    print(first_name + ' ' + last_name)
    
    
generate_my_name(first_name, last_name)
  
  
# Calculating the area of circle
  
def calculate_area_circle(radius):
    PI = 3.14
    calculate = PI * radius * radius
    print(f"The area of Circle is {calculate}")

inp = float(input("Enter the radius of the circle: "))
calculate_area_circle(inp)


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback

def add_all_nums(list):
    count = 0
    for i in list:
        count = i + count
    print(count)

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

print(numbers)
        
add_all_nums(numbers)
        
        
        
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_temp(obj):
    if obj['unit'] in 'C':
        convert_to_farenheit(obj)
    elif obj['unit'] in 'F':
        convert_to_celcius(obj)

def convert_to_celcius(obj):
    print(f"The temperature is {obj['value']}")
    convert = (obj['value'] - 32) * 5/9
    print(f"The temperature converted from {obj['value']}F to {convert}C")
    
def convert_to_farenheit(obj):
    print(f"The temperature is {obj['value']}")
    convert = (9/5 * obj['value']) + 32
    print(f"The temperature converted from {obj['value']}C to {convert}F")
    


val = float(input("Enter the temperature value: "))
unit = input("Enter the unit you want to convert from e.g F or C: ").upper()

obj = { 'value':val, 'unit':unit }
print(obj)
convert_temp(obj);
        
        

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
    
def print_list(lst):
    for i in lst:
        print(i)

my_list = [1, 2, 3, 4, 5]
print_list(my_list)


# Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
    new_list = []
    for i in lst:
        print(i)
        new_list.insert(0,i)
    print(new_list)
    
list = [1,2,3,4,5]

reverse_list(list)
