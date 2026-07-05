#!/usr/bin/python3
# written by: atholcomb
# string_bits.py

def string_bits(str):
  result = ''
  for i in range(len(str)):
    if i % 2 == 0:
      result += str[i]
  return result



print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
