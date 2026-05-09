# In python we can accept user input by using input() function.
# The data type of the input is always string, so we need to convert it into the required data type using Type Casting when needed

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age) # converting the age from string to integer using type casting

# We can accpet user input and type cast it as well in just a single line of code
gpa = float(input("Enter your GPA: "))

age = age + 1

print("Your name is:", name , "Your age is:", age, "Your GPA is:", gpa)
print("---------------------------------------")

# Simple Mad libs Game
color = input("Enter a color: ")
animal = input("Enter an animal: ")
print("The " + color + " " + animal + " jumped over the moon.")

print("---------------------------------------")

# Area of Rectangle 

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")