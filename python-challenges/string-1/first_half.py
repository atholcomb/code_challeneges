#!/usr/bin/python3
# written by: atholcomb
# first_half.py

def first_half(string):
    length = int(len(string) / 2)
    return string[:length]


print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
