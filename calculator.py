# Creating a Simple Calculator in Python
number1 = int(input("Enter the first number: "))
operator = input(": ")
number2 = int(input("Enter the second number: "))

if operator == "+" :
    result = number1 + number2
    print(f"The result is {result}")

if operator == "-":
    result = number1 - number2
    print(f"The result is {result}")

if operator == "*":
    result = number1 * number2
    print(f"The result is {result}")

if operator == "/":
    result = number1 / number2
    print(f"The result is {result}")


print("---------------------------------------")

# User enters: Alice Bob Charlie
a, b, c = input("Enter names: ").split(",")
print("Name 1:", a, "Name 2:", b, "Name 3:", c)