#!/usr/bin/python3
# written by: atholcomb
# near_hundred.py

def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
print(near_hundred(111))
print(near_hundred(-209))
