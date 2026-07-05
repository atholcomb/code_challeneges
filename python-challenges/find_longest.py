#!/usr/bin/python3
# written by: atholcomb
# find_longest.py
# Write a function that will return the longest word in a sentence. 
# In cases where more than one word is found, return the first one.
# Special characters and symbols don't count as part of the word.
# Return the longest word found in lowercase letters.
# A recursive version of this challenge can be found in here.

def find_longest(string):
  # store each word from string into list (words)
  words = string.split()
  count = []

  # count the number of letters for each word and store into count list
  for item in range(len(words)):
    count.append(len(words[item]))

  # compare the length of the each word to the max length of the count list
  # return the longest string
  for w in words:
    if len(w) == max(count):
      return w


print(find_longest("A thing of beauty is a joy forever."))  # forever
print(find_longest("Forgetfulness is by all means powerless!")) # forgetfulness
print(find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel."))  # "strengths"
