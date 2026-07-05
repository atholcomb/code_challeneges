#!/usr/bin/python3
# written by: atholcomb
# in1to10.py

def in1to10(n, outside_mode):
  if n < 2 and outside_mode == False:
    return False
  #elif n >= 1 and n <= 10 and outside_mode == False:
  #  return True
  #elif n <= 1 or n >= 10 and outside_mode == True:
  #  return True
  #elif n <= 1 or n >= 10 and outside_mode == False:
  #  return False
  #else:
  #  return False

print(in1to10(5, False))
#print(in1to10(11, False))
#print(in1to10(11, True))
#print(in1to10(0, False))
#print(in1to10(-1, False))
#print(in1to10(1, False))
