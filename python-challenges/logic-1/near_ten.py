#!/usr/bin/python3
# written by: atholcomb
# near_ten.py

def near_ten(n):
  #num = n + 2
  if n % 10 == 2:
    return True
  return False 


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
