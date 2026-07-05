#!/usr/bin/python3
# written by: atholcomb
# atbash.py
# The Atbash cipher is an encryption method in which each letter 
# of a word is replaced with its "mirror" letter in the alphabet: 
# A <=> Z; B <=> Y; C <=> X; etc.
# Create a function that takes a string and applies the Atbash cipher to it.

def atbash(string):
  cipher = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  # create dictionary comprehension to
  # store numerals + space + !symbol
  numerals_symbols = {x:x for x in " !1234567890"}

  # create list comprehensions and dictionary to
  # store alphabet and reversed alphabet
  standard_alphabet = [letter for letter in alphabet]
  reversed_alphabet = [letter for letter in reversed(alphabet)]
  mirror_standard = dict(zip(standard_alphabet, reversed_alphabet))

  # create list comprehensions and dictionary to
  # store uppercase alphabet and reversed alphabet
  upper_standard_alphabet = [letter.upper() for letter in alphabet]
  upper_reversed_alphabet = [letter.upper() for letter in reversed(alphabet)]
  upper_mirror_standard = dict(zip(upper_standard_alphabet, upper_reversed_alphabet))
  
  # merge lowercase and uppercase dictionaries together 
  mirror_standard.update(upper_mirror_standard)

  # merge numerals + space + !symbol dictionary together
  # with the original alphabet dictionaries
  mirror_standard.update(numerals_symbols)
 
  # create cipher from 'string' input passed in 
  for letter in string:
    cipher += mirror_standard[letter]

  # return solved cipher
  return cipher
    
print(atbash("apple"))  # zkkov
print(atbash("Hello world!")) # Svool dliow!
print(atbash("Christmas is the 25th of December")) # Xsirhgnzh rh gsv 25gs lu Wvxvnyvi
