#!/usr/bin/python3
# written by: atholcomb
# Write a function that finds the sum of the first n natural numbers. Make your function recursive.
# Assume the input number is always positive.
# This version uses a while loop -- see V2, which uses recursion

def sum_numbers(number):
    digits = []
    sum_number = 0

    while number > 0:
        digits.append(number)
        number -= 1

    for s in digits:
        sum_number += s

    return sum_number


print(sum_numbers(5))   # 15 (1 + 2 + 3 + 4 + 5 = 15)
print(sum_numbers(1))   # 1
print(sum_numbers(12))  # 78
