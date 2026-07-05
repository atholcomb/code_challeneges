#!/usr/bin/python3
# written by: atholcomb
# pos_neg.py

def pos_neg(a, b, negative):
  if (a > 0 and b < 0 and negative == False) or (a < 0 and b > 0 and negative == False):
    return True
  elif a < 0 and b < 0 and negative == True:
    return True
  else:
    return False



print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
