# A function is a reusable block of code that can be used anywhere in the file once declared


# def generate_my_name():
#     first_name = "Asadullah"
#     last_name = "yousaf"
#     print(first_name + ' ' + last_name)
    

    
    
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
    
def generate_my_name(first_name, last_name):
    print(first_name + ' ' + last_name)
    
    
generate_my_name(first_name, last_name)