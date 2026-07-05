#!/usr/bin/python3
# written by: atholcomb
# is_sastry.py
# In this challenge, you have to establish if a given integer n is a Sastry number. 
# If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
# Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not

import math

def is_sastry(number):
    concat = number + 1
    concat_str = str(number) + str(concat)

    square = math.ceil(math.sqrt(int(concat_str)))

    if int(concat_str) == (square ** 2):
        return f"{concat_str} is a perfect square ({square} ^ 2)"
    return f"{concat_str} is not a perfect square"


print(is_sastry(183))
print(is_sastry(184))
print(is_sastry(106755))
