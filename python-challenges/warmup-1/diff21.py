#!/usr/bin/python3
# written by: atholcomb
# diff21.py

def diff21(n):
    calc_p = abs((21 - abs(n))) # evaluates positive
    calc_n = abs((21 - n)) # evaluates negative
    if n > 21:
        return calc_p * 2
    elif n < 0:
        return calc_n
    return calc_p
  


print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(22))
print(diff21(25))
print(diff21(-1))
print(diff21(-2))
