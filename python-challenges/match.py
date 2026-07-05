#!/usr/bin/python3
# written by: atholcomb
# match.py
# Write a function that validates whether two strings are identical. Make it case insensitive.

def match(str1, str2):
  
  if str1 == str2.lower():
    return True
  return False


print(match("hello", "hELLo"))      # True
print(match("motive", "emotive"))   # False
print(match("venom", "VENOM"))      # True
print(match("mask", "mAskinG"))     # False
