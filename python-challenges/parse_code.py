#!/usr/bin/python3
# written by: atholcomb
# parse_code.py
# Create a function which takes in an encoded string and returns a dictionary according to the following example:
# The string will always be in the same format: first name, last name and id with zeros between them.
# id numbers will not contain any zeros.
# Bonus: Try solving this using RegEx.

import re

def parse_code(string):
  match = []
  formatting = ["first_name", "last_name", "id"]

  # split the string into a list delimited by the zeros
  zeros = re.split("[00000]", string)
  
  # find and store ONLY the given information needed
  for value in zeros:
    if value != '':
      match.append(value)

  # return a dictionary as asked
  final_result = dict(zip(formatting, match))

  return final_result 


print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
