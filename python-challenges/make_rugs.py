#!/usr/bin/python3
# written by: atholcomb
# make_rugs.py
# Write a function that accepts the height and width (m, n) and an optional proc s,
# and generates a list with m elements. Each element is a string consisting of either:
# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.
# You can set a value for the parameter when creating the function e.g. def func(x = 3)

import json

def make_rug(column, row, char):
  rug = []

  for i in range(column):
    char_times_row = char * row
    rug.append(char_times_row)
  
  return f"make_rug{(column, row, char)} -> {json.dumps(rug, indent=2)}"

print(make_rug(3, 5, '#'))
print(make_rug(3, 5, '$'))
print(make_rug(2, 2, 'A'))

# Answer below illustrates correct output:
'''
make_rug(3, 5, '#') -> [
  "#####",
  "#####",
  "#####"
] 

make_rug(3, 5, '$') -> [
  "$$$$$",
  "$$$$$",
  "$$$$$"
] 

make_rug(2, 2, 'A') -> [
  "AA",
  "AA"
]
'''
