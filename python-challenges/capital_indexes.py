#!/usr/bin/python3
# written by: atholcomb
# capital_indexes.py
# Program returns only the indices which contain capital letters

def capital_indexes(string):
  capitals = {}

  for idx, letter in enumerate(string):
    if letter.isupper():
      capitals[idx] = letter

  return string, capitals

print(capital_indexes('HeLlO'))
print(capital_indexes('HHHHH'))
print(capital_indexes('0192H'))
