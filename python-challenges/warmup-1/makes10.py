#!/usr/bin/python3
# written by: atholcomb
# makes10.py

def makes10(a, b):
    if a + b == 10:
        return True
    elif a == 10 or b == 10:
        return True
    else:
        return False

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))
