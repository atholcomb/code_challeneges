#!/usr/bin/python3
# written by: atholcomb
# list_of_multiples.py
# Create a function that takes two numbers as arguments (num, length) and 
# returns a list of multiples of num until the list length reaches length.

def list_of_multiples(n, m):
  for i in range(1, m+1):
    print(i * n)
  print()

list_of_multiples(7, 5)
list_of_multiples(12, 10)
list_of_multiples(17, 6)
