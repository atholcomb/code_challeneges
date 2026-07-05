#!/usr/bin/python3
# written by: atholcomb
# parse_string_math_operation.py
# Parse strings that for a simple language as follows:
# operations take only 2 params. commands may be nested.
## EXAMPLE INPUT BELOW ##
# input -> "add(1,3)" output -> 4
# input -> "sub(1,3)" output -> -2
# add(sub(3,4), 1) 
# sub(add(238943, 2343), add(1, sub(323, 43)))

def add(int1, int2):
  return int1 + int2

def sub(int1, int2):
  return int1 - int2

def parse_string(string):
  if 'add' in string or 'sub' in string:
    if '"' in string:
      string.replace('"', '') 

  ## convert string into function to pass in to add() or sub()
  return eval(string) 


print(parse_string("add(1,3)"))           # 4
print(parse_string("sub(1,3)"))           # -2
print(parse_string("add(sub(3,4), 1)"))   # 0 
print(parse_string("sub(add(238943, 2343), add(1, sub(323, 43)))"))   # 241005
