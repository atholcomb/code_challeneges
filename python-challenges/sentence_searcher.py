#!/usr/bin/python3
# written by: atholcomb
# sentence_searcher.py
# Create a function that returns the whole of the first sentence which contains a specific word. 
# Include the full stop at the end of the sentence.
# Sentences will always end with full stops.
# Your function should not be case sensitive.
# Return an empty string if the word isn't found in the sentence.

def sentence_searcher(txt, string):
  # make sure all letters in the string are lowercase
  txt = txt.lower()

  # split the string into parts delimited on the period
  phrases = txt.split(".")

  # correct spacing issue from above in indexes 1 and 2
  phrases[1] = phrases[1].lstrip()
  phrases[2] = phrases[2].lstrip()

  # return correct string accordingly, otherwise return empty string
  # correct the final string so that the output is capitalized and includes a period
  for p in range(len(phrases)):
    if string.lower() in phrases[p]:
      return phrases[p].capitalize() + "."
  return '\""'
    

print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "have"))     # I have a cat.
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "MAT"))      # I have a mat.
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "things"))   # Things are going swell.
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "flat"))     # ''
