#!/usr/bin/python3
# written by: atholcomb
# makes10.py
# Create a function that takes two arguments. Both arguments are integers, a and b. 
# Return True if one of them is 10 or if their sum is 10.

def makes10(int1, int2):
  if int1 == 10 or int2 == 10:
      return True
  elif int1 + int2 == 10:
      return True
  else:
      return False


print(makes10(9, 10))   # True
print(makes10(9, 9))    # False
print(makes10(1, 9))    # True
