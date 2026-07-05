#!/usr/bin/python3
# written by: atholcomb
# love6.py

def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif a + b == 6:
    return True
  elif abs(a - b) == 6:
    return True
  else:
    return False


print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))
