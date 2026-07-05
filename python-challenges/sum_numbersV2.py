#!/usr/bin/python3
# written by: atholcomb
# sum_numbersV2.py
# Write a function that finds the sum of the first n natural numbers. Make your function recursive.
# Assume the input number is always positive.
# This version uses recursion, see V1 which uses a while loop

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + (sum_numbers(n - 1))
        

print(sum_numbers(5))   # 15 (1 + 2 + 3 + 4 + 5 = 15)
print(sum_numbers(1))   # 1
print(sum_numbers(12))  # 78
