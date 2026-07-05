#!/usr/bin/python3
# written by: atholcomb
# get_word_length.py
# Given a list words, return the count of the word

def get_word_length(words):
  count = {}

  for word in words:
    count[word] = len(word)
  return count 

print(get_word_length(['dog', 'cat', 'giraffe', 'penguin', 'wolf', 'liger', 'puma']))
