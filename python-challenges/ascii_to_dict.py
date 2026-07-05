#!/usr/bin/python3
# written by: atholcomb
# ascii_to_dict.py
# Given a list of characters, return the ascii 
# code equivalent of the character in a dictionary

def ascii_to_dict(input_list):
  result = dict()

  for item in input_list:
    result[item] = ord(item)

  return result

print(ascii_to_dict(["a", "b", "c"]))
print(ascii_to_dict(["^"]))
print(ascii_to_dict([]))
