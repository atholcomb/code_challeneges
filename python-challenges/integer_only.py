#!/usr/bin/python3
# written by: atholcomb
# integer_only.py
# Given a string with integers and alphabet characters
# parse out the string so only the integers remain

def integer_only(string):

  characters = 'abcdefghijklmnopqrstuvwxyz'
  result = []

  for item in string[:]:
      for letter in item:
          if letter in characters:
              letter.replace(letter, '')
          else: 
              result.append(letter)
  
  return int(''.join(result))


print(integer_only('b101a01'))
print(integer_only('8ll49'))
print(integer_only('-1cd'))
print(integer_only('0p'))
