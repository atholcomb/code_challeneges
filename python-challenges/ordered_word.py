#!/usr/bin/python3
# written by: atholcomb
# ordered_word.py
# Create a function that takes a word as a string and 
# returns a string with its letters in alphabetical order.

def ordered_word(word):
  # formatted output from original word to "alpha-ordered" word
  if len(word) <= 4:
    return f"Original: {''.join(word)} \t\tAlpha-Ordered: {''.join(sorted(word)):<10}"
  return f"Original: {''.join(word)} \tAlpha-Ordered: {''.join(sorted(word)):<10}"

# original word used to create alpha-ordered word
print(ordered_word("hello"))
print(ordered_word("edabit"))
print(ordered_word("hacker"))
print(ordered_word("geeky"))
print(ordered_word("javascript"))
print(ordered_word("in"))
print(ordered_word("joe"))
print(ordered_word("!"))
