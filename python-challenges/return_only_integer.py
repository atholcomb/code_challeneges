#!/usr/bin/python3
# written by: atholcomb
# return_only_integer.py
# Write a function that takes a list of elements and returns only the integers.

def return_only_integer(some_list):
    numbers_only = []

    for item in some_list:
        if type(item) is int:
            numbers_only.append(item)

    return numbers_only

print(return_only_integer([9, 2, "space", "car", "lion", 16]))          # [9, 2, 16]
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String",  True,  3.3,  1]))
