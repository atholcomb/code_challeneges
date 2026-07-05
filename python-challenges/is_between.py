#!/usr/bin/python3
# written by: atholcomb
# is_between.py
# Write a function that takes three string arguments (first, last, and word) and 
# returns True if word is found between first and last in the list, otherwise False.

def is_between(first, last, word):
  words = [first, last, word]
  sorted_words = sorted(words)

  if sorted_words[1] == word:
    return True
  return False


print(is_between("apple", "banana", "azure"))       # True
print(is_between("monk", "monument", "monkey"))     # True
print(is_between("bookend", "boolean", "boost"))    # False
