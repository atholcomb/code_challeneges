#!/usr/bin/python3
# written by: atholcomb
# left2.py

def left2(str):
    left2 = str[:2]

    if len(str) == 2:
        return str
    else:
        return str[2:]+left2

print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))
