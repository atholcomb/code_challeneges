#!/usr/bin/python3
# written by: atholcomb
# string_splosion.py

def string_splosion(str):
    s = len(str)
    value = ''
    while s > 0:
        value += str[:-s]
        s -= 1
    return value + str
    


print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
