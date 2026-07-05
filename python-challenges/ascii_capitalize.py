#!/usr/bin/python3
# written by: atholcomb
# ascii_capitalize.py
# Create a function that takes a string as input and capitalizes a letter if its ASCII 
# code is even and returns its lower case version if its ASCII code is odd.

def ascii_capitalize(string):
  string = string.lower()
  ascii_values = []
  new_string = []
  
  for char in string:
      ascii_values.append(ord(char))

  for av in ascii_values:
      if av % 2 == 0:
          new_string.append(chr(av).upper())
      else:
          new_string.append(chr(av))

  return ''.join(new_string)

print(ascii_capitalize("to be or not to be!"))              # "To Be oR NoT To Be!"
print(ascii_capitalize("THE LITTLE MERMAID"))               # "THe LiTTLe meRmaiD"
print(ascii_capitalize("Oh what a beautiful morning."))     # "oH wHaT a BeauTiFuL moRNiNg."
