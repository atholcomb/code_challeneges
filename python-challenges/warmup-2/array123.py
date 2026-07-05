#!/usr/bin/python3
# written by: atholcomb
# array123.py

def array123(nums):
  for n in nums:
    if 1 and 2 and 3 in nums:
      return True
    return False


print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
