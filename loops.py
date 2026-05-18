# Loops: Loops are used to repeat a block of code multiple times
# To execute a repeatative task we use loops which are of two types:
# 1. For Loop: A for loop is used to iterate over a sequence (like a list, tuple, or string) 
# and execute a block of code for each item in the sequence.
# 2. While Loop: A while loop is used to execute a block of code as long as a specified condition is true.

# While Loop

count = 0

# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print("Loop has ended")


# using break in a while loop

# while count < 5:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count = count + 1
    
    


# A for loop is used to iterate over a sequence (like a list, tuple, or string) 
# and execute a block of code for each item in the sequence.
# language = 'Python'
# for letter in language:
#     print(letter)

# print("-------Next Loop------")
# for i in range(len(language)):
#     print(language[i])

# A loop prints out random results when used on set because sets are unordered lists , where order doesn't matter unlike
# Lists and tuples
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    if company == "IBM":
        break
    print(company)