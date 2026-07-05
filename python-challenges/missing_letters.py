#!/usr/bin/python3
# written by: atholcomb
# missing_letters.py
# Given a string containing unique letters, return a sorted string with the letters that don't appear in the string.

def get_missing_letters(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    not_in_string = ''

    for letter in letters:
        if letter not in string:
            not_in_string += letter

    return not_in_string


print(get_missing_letters("abcdefgpqrstuvwxyz")) # "hijklmno"
print(get_missing_letters("zyxwvutsrq")) # "abcdefghijklmnop"
print(get_missing_letters("abc")) # "defghijklmnopqrstuvwxyz"
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz")) # "" or empty string
