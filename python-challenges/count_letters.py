#!/usr/bin/python3
# written by: atholcomb
# count_letters.py
# count the number of characters for each string given

def count_letters(string):
  result = {}

  for s in string:
    result[s] = string.count(s)

  return result

print(count_letters("AaBbCc"))              # Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4"))  # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence.")) # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
