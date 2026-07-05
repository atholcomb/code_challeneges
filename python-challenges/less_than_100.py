#!/usr/bin/python3
# written by: atholcomb
# less_than_100.py
# Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.

def less_than_100(int1, int2):
    
    if int1 + int2 < 100:
        return f"{int1} + {int2} = {int1 + int2} -> True"
    else:
        return f"{int1} + {int2} = {int1 + int2} -> False"

print(less_than_100(22, 15))    # True
print(less_than_100(83, 34))    # False
print(less_than_100(3, 77))     # True
