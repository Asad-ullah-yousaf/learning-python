# What is a Module
# A module is a file containing a set of codes or a set of functions which can be included to an application. 
# A module could be a file containing a single variable, a function or a big code base.

# from random import random, randint
# from math import floor, ceil

# print(floor(random()*256))
# print(randint(1, 10))

import string
import math
import random

# str = string.ascii_letters
# # print(str)

# number = string.digits
# # print(number)

# combination = str + number
# # print(combination)

# list_of_uids = []

# def generate_random_uid(combination):
#     id = []
#     while len(id) < 6:
#        ran = random.randint(0, 61)
#        id.append(combination[ran])
#     print("Random Id",id)
   
#     uid = ''.join(id)
#     print("Random generated UId",uid)
#     list_of_uids.append(uid)
    
    
     
# for i in range(5):
#     print('---------')
#     generate_random_uid(combination)

# print(list_of_uids)

num_of_ids = int(input("How many ids to generate: "))
lst_of_ids = []
def generate_user_id():
    char_of_id = int(input("Number of characters the id should have: "))
    
    
    comb = string.ascii_letters + string.digits
    ids = []
    while len(ids) < char_of_id:
        random_num = random.randint(0,61)
        ids.append(comb[random_num])
    print(ids)
    new = ''.join(ids)
    lst_of_ids.append(new)
    
        
        
for i in range(num_of_ids):
    generate_user_id()
    print('-------')
    
print(lst_of_ids)