#!/usr/bin/python3
# written by: atholcomb
# letter_only.py
# Check if the given string consists of only letters and spaces and if every letter is in lower case.

numbers = '0123456789'

def letters_only(string):
    for n in numbers:
        if n in string:
            return string, False
        elif string == string.upper():
            return string, False
        else:
            return string, True

print(letters_only("PYTHON"))
print(letters_only("python"))
print(letters_only("12321313"))
print(letters_only("i have spaces"))
print(letters_only("i have numbers(110)"))
print(letters_only(""))
