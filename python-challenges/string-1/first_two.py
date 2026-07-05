#!/usr/bin/python3
# written by: atholcomb
# first_two.py

def first_two(str):
    f2 = str[:2]
    
    if len(str) < 2:
        return str
    else:
        return f2

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))

