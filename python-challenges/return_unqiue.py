#!/usr/bin/python3
# written by: atholcomb
# return_unqiue.py
# In each input list, every number repeats at least once, except for two. 
# Write a function that returns the two unique numbers.

def return_unique(lst):
    result = []

    for item in lst:
        if lst.count(item) == 1:
            result.append(item)

    return result

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6])) # [9, 7]
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])) # [2, 1]
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])) # [5, 6]
