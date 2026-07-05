#!/usr/bin/python3
# written by: atholcomb
# valid_pin.py
# Create a function to test if a string is a valid pin or not.
# A valid pin has:
# Exactly 4 or 6 characters. Only numerical characters (0-9).
# No whitespace. Empty strings should return False when tested.

def valid_pin(string):
  numerals = '0123456789'
  chars = 'abc'
  
  for num in numerals:
    if chars not in string and ' ' not in string:
      if len(string) == 4 or len(string) == 6:
        return True
    return False
    

print(valid_pin("1234"))    # True
print(valid_pin("45135"))   # False
print(valid_pin("89abc1"))  # False
print(valid_pin("900876"))  # True
print(valid_pin(" 4983"))   # False
