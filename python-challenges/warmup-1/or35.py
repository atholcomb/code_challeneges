#!/usr/bin/python3
# written by: atholcomb
# or35.py

def or35(n):
    if n % 3 == 0:
        return str(n) + " is a multiple of 3"
    elif n % 5 == 0:
        return str(n) + " is a multiple of 5"
    else:
        return str(n) + " is not a multiple of 3 or 5"


print(or35(3))
print(or35(10))
print(or35(8))
