#!/usr/bin/python3
# written by: atholcomb
# is_pandigital.py
# A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, 
# returning True if the integer is pandigital, and False otherwise.

def is_pandigital(number):
    str_num = str(number)
    
    for value in '0123456789':
        if value not in str_num:
            return f"{False}, missing {value}"
    return True
        

print(is_pandigital(98140723568910))        # True
print(is_pandigital(90864523148909))        # False, missing 7
print(is_pandigital(112233445566778899))    # False, missing 0
