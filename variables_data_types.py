# Variables : Variables include 4 types of data types ( String, Integer, Float , Boolean)
#  Each variable has the data type based on the value it is assigned with so we don't need to specify the data type of any variable

# String
name = "Asad"
course = "Learning python"
print(name)
print(course)

# Integer
age = 20
year = 2026
print(age)
print(year)

# Float 
temperate_of_body = 98.6
pi = 3.14
print(temperate_of_body)
print(pi)

# Boolean
is_adult = True
is_student = False
print(is_adult)
print(is_student)

# There is another interesting way to print our variables with the help of f-string which is used to format the string and include variables in it
print(f"My name is {name} and I am {course}.")
print(f"I am {age} years old and the year is {year}.")
print(f"The temperate of body is {temperate_of_body} and the value of pi is {pi}.")
print(f"Is it true that I am an adult? {is_adult} and is it true that I am a student? {is_student}.")


string = b'a\x01c'
print(string)