# building a temperature converter that converts temperature from celsius to fahrenheit and vice versa.

temp = float(input("Enter the temperature you want to convert (e.g. 37): "))
unit = input("Enter the unit of the temperature you want to convert (C for celsius and F for fahrenheit): ").upper()

tempObj = { 'value':temp, 'unit':unit }
print(f"The temperature you entered is {tempObj['value']} {tempObj['unit']}")

if tempObj['unit'] in ('C'):
    C = tempObj['value']
    celcius = (C * 9/5) + 32
    print(f"The Temperature is converted from C to {celcius} F")
elif tempObj['unit'] in ('F'):
    F = tempObj['value']
    farenheit = (F - 32) * 5/9
    print(f"The temperature was converted from Farenheit to {farenheit} C")
else:
    print("Invalid Input")


# String Manipulation : String Splicer and shifter

# string = "Python"
# print(string[0:4])
# print(string[4:6])
# print(string[::-1])


# Problem 3: The Library Fee Calculator

days_late = int(input("Enter the number of days late: "))
fine_amount = 0;

if days_late <= 5 and days_late != 0:
    total_fine = fine_amount + days_late
    print(f"you returned book {days_late} days late and your total fine will be $ {total_fine}")
elif days_late >= 6 :
    total_fine = (fine_amount + days_late) * 2
    print(f"you returned book {days_late} days late and your total fine will be $ {total_fine}")
elif days_late < 1:
    print("Please enter a valid input")
else:
    print("Please enter a valid input")
    
    
    
# Problem 4: The Bouncer List
#     The Goal: Modify and filter a list.
#     What to do: Start with a list of numbers representing ages: ages = [16, 21, 18, 30, 15, 25].
#         Add a new age (22) to the end of the list.
#         Remove the youngest age (15) from the list.
#         Bonus challenge: Create a new empty list called adults. Loop through your ages list, and if an age is 18 or older, append it to the adults list.

ages = [16, 21, 18, 30, 15, 25]
ages.append(22)
print(ages)


ages.remove(min(ages))
print(ages)

adults = []

for i in ages:
    if i >= 18:
        adults.append(i)
print(adults)


# Problem 5: Coordinates (Tuple Exploration)
#     The Goal: Understand tuple immutability and unpacking.
#     What to do: Create a tuple representing a 2D coordinate: point = (4, 10).
#         Try to change the first value to 5 and observe the error Python gives you.
#         Unpack the tuple into two separate variables, x and y, and print them.

point = (4, 10)
x = point[0]
y = point[1]

point[0] = 5
print(x)
print(y)




# 4. Mapping Data (Dictionaries)
# Problem 6: The Inventory Update
#     The Goal: Access, add, and modify dictionary key-value pairs.
#     What to do: Create a dictionary representing a store's fruit stock:
#     stock = {"apples": 10, "bananas": 4, "oranges": 8}
#         The store just bought 5 more bananas. Update the "bananas" count.
#         The store started selling "mangos". Add "mangos" to the dictionary with an initial stock of 12.
#         Print the final dictionary.

fruit_stock = { "Apples": 10, "Bananas": 4, "Oranges": 8 }
fruit_stock.update({'Bananas':9})
fruit_stock.update({"Mangos":12})
print(fruit_stock)