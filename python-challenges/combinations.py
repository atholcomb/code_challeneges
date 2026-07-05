#!/usr/bin/python3
# written by: atholcomb
# combinations.py
# Create a function that takes a variable number of groups of items, and returns the 
# number of ways the items can be arranged, with one item from each group. Order does not matter.

def combinations(*args):
  result = 1

  for values in args:
    result *= values

  return result

print(combinations(2, 3)) # 6
print(combinations(3, 7, 4)) # 84
print(combinations(2, 3, 4, 5)) # 120
