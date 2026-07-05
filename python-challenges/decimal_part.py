#!/usr/bin/python3
# written by: atholcomb
# decimal_part.py
# Create a function which takes a number n and return its decimal part.

def decimal_part(float_num):
  # create str object out of float_num to enumerate over
  float_str = str(float_num)
  
  # find the position where the decimal is at
  # return str with decimal part only
  # else return n
  for idx, fstr in enumerate(float_str):
    if '.' in float_str[idx]:
      return f'{float_str[idx:]}'
  return 0
        

print(decimal_part(1.2))    # .2
print(decimal_part(-3.73))  # .73
print(decimal_part(10))     # 0
