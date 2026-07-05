#!/usr/bin/python3
# written by: atholcomb
# letter_before.py
# Write a function that changes every letter to the letter before it

def letter_before(string):
    original_string = string
    temp = 0 # store letter unicode integer value to decrement in for loop

    for letter in string:
        temp = ord(letter)
        string = string.replace(letter, chr(temp-1))

    return f"{original_string} -> {string}"


print(letter_before("hello")) # gdkkn
print(letter_before("bye")) # axd
print(letter_before("welcome")) # vdkbnld
