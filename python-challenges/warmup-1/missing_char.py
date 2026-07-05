#!/usr/bin/python3
# written by: atholcomb
# missing_char.py

def missing_char(str, n):
    char = str[n]
    return str.replace(char, '')



print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))
