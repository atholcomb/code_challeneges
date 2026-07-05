#!/usr/bin/python3
# written by: atholcomb
# is_symmetrical.py
# Create a function that takes a number as an argument and returns True or False 
# depending on whether the number is symmetrical or not. 
# A number is symmetrical when it is the same as its reverse.

def is_symmetrical(number):
    # make number a string so we can reverse it below
    number = str(number)
    
    # compare original number to it's reversed value and return True or False
    if number == number[::-1]:
        return True
    return False


print(is_symmetrical(7227))         # True
print(is_symmetrical(12567))        # False
print(is_symmetrical(44444444))     # True
print(is_symmetrical(9939))         # False
print(is_symmetrical(1112111))      # True
